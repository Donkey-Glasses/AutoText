# This is a simple tool to make sure I build json files correctly

import json


FILE_NAME = 'default.options'
ITEM_DICT = {'char_width': 120}


def write_json(file_name, item_dict):
    with open(file_name, 'w+') as f:
        json.dump(item_dict, f, indent=4)


if __name__ == "__main__":
    write_json(FILE_NAME, ITEM_DICT)
