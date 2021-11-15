import bs4
import pandas as pd
import requests
import json
    
url = 'https://scikit-learn.org/stable/modules/classes.html'
module_url = "https://scikit-learn.org/stable/modules/"

def get_page_contents(url):
    page = requests.get(url, headers={"Accept-Language": "en-US"})
    return bs4.BeautifulSoup(page.text, "html.parser")


def check_if_method(name):
    if name[0].isupper():
        return False, True
    else:
        return True, False



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
        elements = table.findAll("a", class_="reference internal")
        for elem in elements:
                try:
                    is_method, is_class = check_if_method(elem["title"].split(".")[-1])
                    module = {"package_name": name,
                              "full_name": elem["title"], 
                              "name": elem["title"].split(".")[-1], 
                              "href": elem["href"],
                              "is_method": is_method,
                              "is_class": is_class
                              }
                    print(module["name"], module["is_method"])
                except KeyError:
                    pass
                finally:
                    data.append(module)

print("number of modules: ", len(names))
print("number of classes/function", len(data))


with open("modules.json", "w") as f:
    json.dump(data, f)


