#!/usr/bin/python3
def save_to_json_file(my_obj, filename):
    import json
    with open(filename, mode="w") as myFile:
        json.dump(my_obj, myFile)
