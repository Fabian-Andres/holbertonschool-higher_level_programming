#!/usr/bin/python3
"""[load_save_json_file function]"""
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


try:
    file = load_from_json_file("add_item.json")
except:
    file = []

for i in range(1, len(argv)):
    l.append(argv[i])

save_to_json_file(l, "add_item.json")
