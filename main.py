import Locations
import Characters

from json import load
from random import choice


game_options = {}


def read_options(options_file: str):
    with open(options_file) as options:
        global game_options
        game_options = load(options)


class OptionList:
    raise NotImplementedError


def rand_from_json(file_name, key):
    with open(file_name) as f:
        json_data = load(f)
        return choice(json_data[key])


def load_from_data_file(data_file):
    with open(data_file) as f:
        data = load(f)
        return data


if __name__ == '__main__':
    print('main')
