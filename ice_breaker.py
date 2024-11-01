from dotenv import load_dotenv
import os
from output_parser import summary_parser
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from third_parties.linkedin import scrape_linkedin_profile


def ice_break_with(name: str) -> str:
    linked_data=scrape_linkedin_profile(linked_url="https://www.linkedin.com/in/myat-htut/",mock=True)

    summary_template = """
    given the information about a person from linkedin {information},
    1. A short summary
    2. two interesting facts about them 

    Use both information from twitter and Linkedin
    \n{format_instructions}
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information", "twitter_posts"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")

    chain = summary_prompt_template | llm | summary_parser

    res = chain.invoke(input={"information": linked_data})

    print(res)
    

if __name__ == "__main__":
    load_dotenv()

    print("Ice Breaker Enter")
    ice_break_with(name="Myat Htut Thu")
    
    # information = """
    
    # """

    # load_dotenv()
    # print("hello langchain")
    # # print(os.environ["OPENAI_API_KEY"])
    # summary_template = """
    # give the linkedin information {information} I want to create.
    # 1. a short summary
    # 2. two interesting fact.
    # \n{format_instruction}
    # """
    # summary_prompt_template = PromptTemplate(
    #     input_variables=["information"], template=summary_template,
    #     partial_variables={"format_instruction":summary_parser.get_format_instructions()}
    # )
    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    # # llm = ChatOllama(model="mistral")
    # # llm = ChatOllama(model="llama3")
    # linked_data=scrape_linkedin_profile(linked_url="https://www.linkedin.com/in/myat-htut/",mock=True)
    # chain = summary_prompt_template | llm|summary_parser
    # res = chain.invoke(input={"information": linked_data})
