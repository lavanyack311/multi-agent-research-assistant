from agents import build_web_scrape, build_web_search, critic_chain, writer_chain
from langchain.messages import ToolMessage

def run_research_pipeline(topic:str)->dict:

    state={}

    ##agent started working.

    print("\n"+"="*50)
    print("agent started.......")
    print("="*50)

    search_agent=build_web_search()
    search_results=search_agent.invoke({
        "messages":[(
            "user",f"Search the most recent and reliable information about the {topic}"
        )]
    })

    tool_output=[
        msg.content
        for msg in search_results['messages']
        if isinstance(msg,ToolMessage)
    ]

    state['search_results']="\n_\n".join(tool_output)
    print("\nSEARCH RESULTS:\n",state['search_results'])

   #reader agent

    print("\n"+"="*50)
    print("Scraping the top most resources.......")
    print("="*50)

    reader_agent=build_web_scrape()
    reader_result=reader_agent.invoke({
        "messages":[(
            "user",f"Based on the search about the information on a {topic}\n"
            f"Select the most relavant and recent urls and scrape the content for deeper reading\n\n"
            f"\nSearch Results\n,{state['search_results'][:5000]}"
        )]
    })

    state['scraped_content']=reader_result['messages'][-1].content
    print("\nSCRAPED CONTENT:\n\n",state['scraped_content'])

    # writer chain

    print("\n"+"="*50)
    print("writing the report.......")
    print("="*50)

    research_gathered=(
        f"Search Results\n {state['search_results']}"
        f"Scrapped Content\n {state['scraped_content']}"
    )

    state['report']=writer_chain.invoke({
        "topic":topic,
        "report":research_gathered
    })

    print("\n REPORT\n",state['report'])

    #critic chain

    print("\n"+"="*50)
    print("reviewing the report.......")
    print("="*50)

    state['feedback']=critic_chain.invoke({
        "report":state['report']
    })

    print("\n FEEDBACK \n",state["feedback"])
    return state


if __name__=="__main__":
    topic=input("Enter the topic:")
    run_research_pipeline(topic)