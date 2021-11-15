import bs4
import pandas as pd
import requests
import json
from enum import Enum

class ModuleType(Enum):
    METHOD = 1
    CLASS = 2
    DECORATOR =  3


print(ModuleType.CLASS)

url = 'https://scikit-learn.org/stable/modules/classes.html'
module_url = "https://scikit-learn.org/stable/modules/"

def get_page_contents(url):
    page = requests.get(url, headers={"Accept-Language": "en-US"})
    return bs4.BeautifulSoup(page.text, "html.parser")


def check_type(name):
    if name[0].isupper():
        return ModuleType.CLASS.name
    else:
        return ModuleType.METHOD.name


soup = get_page_contents(url)

api_ref = soup.find("section", id="api-reference")

sections = api_ref.findAll("section")

names = [module["id"] for module in sections if module["id"].startswith(("module", "sklearn")) and not module["id"].endswith(("image", "text"))]

data = []

for name in names:
    base = soup.find("section", id=name)
    print("==================================================")
    print("name: ", name)
    tables = base.findAll("table", class_="docutils")    
    for table in tables:
        rows = table.findAll("tr")
        for tr in rows:
            entries = tr.findAll("td")
            entry = entries[0]
            description = entries[-1].find("p").text
            
            element = entry.find("a", class_="reference internal")
            module_type = check_type(element["title"].split(".")[-1])
            module = {"package_name": name,
                      "description": description,
                      "full_name": element["title"], 
                      "name": element["title"].split(".")[-1], 
                      "href": element["href"],
                      "type": module_type ,
                      }
            print(module["name"])
            data.append(module)

print("number of modules: ", len(names))
print("number of classes/function", len(data))


with open("modules.json", "w") as f:
     json.dump(data, f, sort_keys=True, indent=4)


