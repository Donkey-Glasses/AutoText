from json import load
from random import choice


class OptionList:
    def __init__(self):
        raise NotImplementedError


def rand_from_json(file_name, key):
    with open(file_name) as f:
        json_data = load(f)
        return choice(json_data[key])


def load_from_data_file(data_file):
    with open(data_file) as f:
        data = load(f)
        return data
