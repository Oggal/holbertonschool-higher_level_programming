#!/usr/bin/python3
'''Beam me the file scotty!'''

load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file


def add_item(items=[]):
    try:
        the_list = load("add_item.json")
    except IOError:
        the_list = []
    for item in items:
        the_list.append(item)
    save(the_list, "add_item.json")

if __name__ == "__main__":
    import sys
    add_item(sys.argv[1:])
