from dotenv import load_dotenv
from tavily import TavilyClient
import os
import requests
from bs4 import BeautifulSoup
from langchain.tools import tool
from rich import print

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query:str)->str:
    """Searches the most recent and reliable information about a topic and returns the urls, title and snippets"""
    resuluts=tavily.search(
        query=query,
        max_results=5
    )

    out=[]
    for r in resuluts['results']:
        out.append(
            f"TITLE:{r['title']}\nURL{r['url']}\nSNIPPET:{r['content'][:3000]}\n"
        )

    return "\n_\n".join(out)
@tool
def web_scrape(url:str)->str:
    """Scrapes the urls and extract the information in readeing format for deeper reading"""
    try:
        response= requests.get(url,timeout=8,headers={"User-Agent": "Mozilla/5.0"})
        soup =BeautifulSoup(response.text,"html.parser")
        for tag in soup("nav","header","footer","script"):
            tag.decompse()
        return soup.getText(separator=" ",strip=True)[:3000]
    except Exception as err:
        return f"An excpetion is raised due to {err})"

# print(web_search.invoke("What is the latest incident on IRAN-US War"))
# print(web_scrape.invoke("https://www.bbc.com/news/articles/cvgzzn4y1n8o"))

