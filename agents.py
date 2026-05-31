from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import create_agent
from tools import web_scrape,web_search

load_dotenv()
llm= ChatMistralAI(model="mistral-small-2506")
parser=StrOutputParser()

# create agents


def build_web_search():
    return create_agent(
        model = llm,
        tools= [web_search]
    )

def build_web_scrape():
    return create_agent(
        model=llm,
        tools=[web_scrape]
    )

#writer chain

writer_prompt=ChatPromptTemplate.from_messages([
    "system","You are an research expert. Write the reasearch report on",
    "human","""
    Write a research report in below format.
    topic:{topic}
    Research Gathered:{report}

    -Introduction
    -Key findings(3 minimum detailed points)
    -Takeways
    -Conculsion

    Be proffesional and clean
"""
])

writer_chain= writer_prompt | llm | parser

## critic chain

critic_prompt=ChatPromptTemplate.from_messages([
    "system","You are an critic expert, write a review on a research.",
    "human","""
Write a review on the research report in below mentioned format:

report: {report}

Score:X/10:


Areas of Strength:
.------
.-------

Areas to improve:
.--------
.--------

Final Verdict...

Be honest and specific """
])

critic_chain = critic_prompt | llm | parser
