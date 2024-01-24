#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if my_list == search else my_list for my_list in my_list]
