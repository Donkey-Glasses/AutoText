import Locations
import Characters

from json import load
from random import choice


GAME_OPTIONS = {}


def read_options(options_file: str):
    with open(options_file) as options:
        GAME_OPTIONS = load(options)


class OptionList:
    raise NotImplementedError


def rand_from_json(file_name, key):
    with open(file_name) as f:
        json_data = load(f)
        return choice(json_data[key])


if __name__ == '__main__':
    print('main')
