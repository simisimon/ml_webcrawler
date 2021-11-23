import os
import bs4
import requests

def get_page_contents(url):
    page = requests.get(url, headers={"Accept-Language": "en-US"})
    return bs4.BeautifulSoup(page.text, "html.parser")


def extract_params(href, module_type):

    if module_type != "CLASS":
        return []
    
    url = os.path.join("https://scikit-learn.org/stable/modules/", href)
    print(url)

    soup = get_page_contents(url)
    try:
        table = soup.findAll("dl", class_="field-list")[0]

        not_param = table.findAll("dt")[0]

        if not_param.text != "Parameters":
            return []

        param_sec = table.findAll("dd")[0]

        param_entities = param_sec.findAll("dt")

        params = []

        for param_entity in param_entities:
            param = param_entity.find("strong")
            if param:
                params.append(param.text)

        return params
    except Exception as e:
        print(e)
        return []