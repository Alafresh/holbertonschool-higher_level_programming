#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    return [replace if search is x else x for x in new_list]
