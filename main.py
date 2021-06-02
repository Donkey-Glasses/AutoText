import Locations
import Characters

from json import load


game_options = {}


def read_options(options_file: str):
    with open(options_file) as options:
        global game_options
        game_options = load(options)


if __name__ == '__main__':
    print('main')
