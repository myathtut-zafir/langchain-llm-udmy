import os
import requests
from dotenv import load_dotenv


def scrape_linkedin_profile(linked_url:str,mock:bool=False):
    """sumary_line
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if mock:
        linked_url = "https://gist.githubusercontent.com/myathtutthu-genie/09bceec87900668191ff90cc020a6910/raw/c7cf224446e34b021a882bbfc070d708047a7e75/gistfile1.txt"
        response=requests.get(linked_url,timeout=10)
    else:
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response = requests.get(
            api_endpoint,
            params={"url": linked_url},
            headers=header_dic,
            timeout=10,
        )

    data=response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    


    return data
     
    
# print(scrape_linkedin_profile("https://www.linkedin.com/in/myat-htut/",True))