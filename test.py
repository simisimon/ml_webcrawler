import bs4
import pandas as pd
import requests

from typing import List
from dataclasses import dataclass
from sci_kit_learn_modules import Module, SciKitLearnModule
    
url = 'https://scikit-learn.org/stable/modules/classes.html'
def get_page_contents(url):
    page = requests.get(url, headers={"Accept-Language": "en-US"})
    return bs4.BeautifulSoup(page.text, "html.parser")

soup = get_page_contents(url)

api_ref = soup.find("section", id="api-reference")

sections = api_ref.findAll("section")

modules = [module["id"] for module in sections if module["id"].startswith(("module", "sklearn")) and not module["id"].endswith(("image", "text"))]

data = []

for name in modules:
    base = soup.find("section", id=name)
    sklearn_module = SciKitLearnModule(name=name, modules=[])
    sections = base.findAll("section")
    if sections:
        print(name)
        for section in sections:
            print("==", section["id"])
            modules = section.findAll("a", class_="reference internal")
            for module in modules:
                try:
                    elem = Module(module["title"], module["href"])
                    sklearn_module.modules.append(elem)
                except KeyError:
                    print("continue")

    data.append(sklearn_module)



