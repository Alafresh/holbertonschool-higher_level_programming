#!/usr/bin/python3
from sys import argv
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

try:
    myFile = load_from_json_file("add_item.json")
except FileNotFoundError:
    myFile = []
finally:
    for i in range(1, len(argv)):
        myFile.append(argv[i])
    save_to_json_file(myFile, "add_item.json")
