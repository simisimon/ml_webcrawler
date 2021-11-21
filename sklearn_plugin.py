from ast import Assign, Call, Name, keyword
import ast
import json
import re
import os 

class SciKitLearnPlugin:
    import_reg = re.compile(r"import sklearn")
    import_from_reg = re.compile(r"from sklearn[a-zA-z._]* import [a-zA-Z_]*")

    def __init__(self, concept_name: str):
        self.concept_name = concept_name

    def is_responsible(self, abs_file_path: str) -> bool:
        if not abs_file_path.endswith(".py"):
            return False

        with open(abs_file_path, "r") as source:
            for line in source.readlines():
                if SciKitLearnPlugin.import_reg.match(line):
                    print("here")
                    return True
                if SciKitLearnPlugin.import_from_reg.match(line):
                    return True
                    
    def parse_file(self, abs_file_path):
        pass

def main():
    f = open("modules.json", "r")
    data = json.load(f)
    f.close()

    module_names = [x["name"] for x in data if x["type"] == "CLASS"]

    with open("sklearn_test.py", "r") as source:
        tree = ast.parse(source.read())

    for node in ast.walk(tree):
        if isinstance(node, Assign):
            obj = node.value
            if isinstance(obj, Call):
                name = obj.func
                keywords = obj.keywords
                if isinstance(name, Name):
                    print("=========================")
                    if name.id in module_names:
                        print("name.id: ", name.id)
                    for key in keywords:
                        if isinstance(key, keyword):
                            print("keyword.arg: ", key.arg)
                            print("keyword.value: ", key.value.value)

    plugin = SciKitLearnPlugin("Sklearn")
    print(plugin.is_responsible(os.path.abspath("sklearn_test.py")))


if __name__ == "__main__":
    main()


