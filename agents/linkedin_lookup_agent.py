from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (create_react_agent,AgentExecutor)
from langchain import hub

# from tools.tools import get_profile_url_tra
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()
def lookup(name:str)->str:
    llm=ChatOpenAI(temperature=0,
                   model_name="gpt-4o-mini")
    template = """given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page.
                              Your answer should contain only a URL"""
    prompt_template=PromptTemplate(template=template,input_variables=["name_of_person"])
    
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url_tra,
            description="useful for when you need get the Linkedin Page URL",
        )
    ]
    react_prompt=hub.pull('hwchase17/react')
    agent=create_react_agent(llm=llm,tools=tools_for_agent,prompt=react_prompt)# create agent
    agent_executor=AgentExecutor(agent=agent,tools=tools_for_agent,verbose=True)# this is run the agent
    
    result=agent_executor.invoke(input={'input':prompt_template.format_prompt(name_of_person=name)})
    linked_profile_url=result["output"]
    
    return linked_profile_url

def get_profile_url_tra(name:str):
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res

if __name__=="__main__":
    print(lookup(name="myat-htut"))
    
    
    