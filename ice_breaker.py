from dotenv import load_dotenv
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    information = """
    
    """

    load_dotenv()
    print("hello langchain")
    # print(os.environ["OPENAI_API_KEY"])
    summary_template = """
    give the linkedin information {information} I want to create.
    1. a short summary
    2. two interesting fact.
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    # llm = ChatOllama(model="mistral")
    # llm = ChatOllama(model="llama3")
    linked_data=scrape_linkedin_profile(linked_url="https://www.linkedin.com/in/myat-htut/",mock=True)
    chain = summary_prompt_template | llm|StrOutputParser()
    res = chain.invoke(input={"information": linked_data})

    print(res)
