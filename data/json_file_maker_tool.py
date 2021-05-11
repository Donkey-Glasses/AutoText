# This is a simple tool to make sure I build json files correctly

import json


FILE_NAME = 'characters.data'
ITEM_DICT = {'Species':
             {'human': {'species': 'human', 'scientific': 'homonus', 'adjective': 'human', 'plural': 'humans',
                        'epithet': 'jack', 'epithet_plural': 'jacks', 'mods': [1, 1, 1, 1, 1, 1]},
              'dwarf': {'species': 'dwarf', 'scientific': 'dwarvus', 'adjective': 'dwarven', 'plural': 'dwarves',
                        'epithet': 'dung', 'epithet_plural': 'dungs', 'mods': [2, 0, 2, 0, 0, 0]},
              'elf': {'species': 'elf', 'scientific': 'elvynus', 'adjective': 'elven', 'plural': 'elves',
                      'epithet': 'ear', 'epithet_plural': 'ears', 'mods': [0, 2, 0, 2, 0, 0]},
              'goblin': {'species': 'goblin', 'scientific': 'gobican', 'adjective': 'goblin', 'plural': 'goblins',
                         'epithet': 'gib', 'epithet_plural': 'gibs', 'mods': [0, 2, 0, 0, 0, 0]}},
             'Gender':
                 {'non-binary': {'scientific': 'non-binary', 'adult': 'person', 'diminutive': 'child',
                                 'objective': 'they', 'subjective': 'them'},
                  'female': {'scientific': 'female', 'adult': 'woman', 'diminutive': 'girl',
                             'objective': 'she', 'subjective': 'her'},
                  'male': {'scientific': 'male', 'adult': 'man', 'diminutive': 'boy',
                           'objective': 'he', 'subjective': 'him'},
                  'object': {'scientific': 'object', 'adult': 'object', 'diminutive': 'object',
                             'objective': 'it\'s', 'subjective': 'it'},
                  }
             }


def write_json(file_name, item_dict):
    with open(file_name, 'w+') as f:
        json.dump(item_dict, f, indent=4)


if __name__ == "__main__":
    write_json(FILE_NAME, ITEM_DICT)
