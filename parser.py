from ast import Assign, Call, Name, keyword, Expr, Constant, Tuple, List, Module, Import, FunctionDef
import ast
import json
import re
import os


def parse_assign(node, module_names):
    print(type(node))
    obj = node.value
    if isinstance(obj, Call):
        name = obj.func
        keywords = obj.keywords
        args = obj.args

        print("name type: ", type(name))
        print("keywords: ", keywords)
        print("args: ", args)

        if isinstance(name, Name):
            print("=========================")
            if name.id in module_names:
                print("name.id: ", name.id)
            for arg in args:
                if arg:
                    if isinstance(arg, Name):
                        print(arg.id)
                    if isinstance(arg, List):
                        list_value = []
                        for elem in arg.elts:
                            if isinstance(elem, Tuple):
                                tuple_values = []
                                for val in elem.elts:
                                    if isinstance(val, Constant):
                                        tuple_values.append(val.value)
                                    if isinstance(val, Call):
                                        tuple_values.append(val.func.id)
                                    if isinstance(val, Name):
                                        tuple_values.append(val.id)
                                list_value.append(tuple(tuple_values))

            for key in keywords:
                if isinstance(key, keyword):
                    value = key.value
                    print(type(value))
                    if isinstance(value, Tuple):
                        print("elts:", value.elts)
                    if isinstance(value, Constant):
                        print(value.value)

def parse_expression(node, module_name):
    if isinstance(node, Expr):
        obj = node.value
        if isinstance(obj, Call):
            arg = obj.args[0]
            if isinstance(arg, Call):
                arg_name = arg.func
                keywords = arg.keywords
                args = arg.args
                if isinstance(arg_name, Name):
                    print(arg_name.id)
                if not keywords:
                    for arg in args:
                        if isinstance(arg, Constant):
                            print(arg.value)
                else:
                    for key in arg.keywords:
                        if key and isinstance(key, keyword):
                            value = key.value
                            #if isinstance(value, Tuple):
                            #print("keyword.value: ", key.value.value)
                    

def main():
    #f = open("modules_all.json", "r")
    #data = json.load(f)
    #f.close()

    #module_names = [x["name"] for x in data if x["type"] == "CLASS"]

    with open("sklearn_test.py", "r") as source:
        tree = ast.parse(source.read())

    for node in ast.walk(tree):
        print(node)
        #if isinstance(node, Assign):
        #    parse_assign(node, module_names)
        #if isinstance(node, Expr):
        #    parse_expression(node, module_names)

        #if isinstance(node, Call):
        #    arg_name = node.func
        #    keywords = node.keywords
        #    args = node.args
        #    if isinstance(arg_name, Name):
        #        print(arg_name.id)

        
        if isinstance(node, FunctionDef):
            print("name:", node.name)
            print("args:", node.args)
            print("body:", node.body)
            print("decorator", node.decorator_list)
            decorators = node.decorator_list
            for deco in decorators:
                if isinstance(deco, Name):
                    print("name.id:", deco.id)

if __name__ == "__main__":
    main()


