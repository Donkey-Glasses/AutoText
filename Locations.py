from typing import List

from helpers import OptionList
# from Characters import Hero, NonPlayer


class Location:
    def __init__(self, location_name: str, description: str, option_list: OptionList, npc_list: List):
        self.location_name = location_name
        self.description = description
        self.option_list = option_list
        self.npc_list = npc_list

    def on_enter(self, player):
        print(self.location_name.center(40, '*'))
        print(self.description)
        print('-' * 40)
        for npc in self.npc_list:
            print(f'  {npc.last_name}')
            print(f'  {npc.description}')


class Dungeon(Location):
    def __init__(self, location_name, description, option_list, npc_list):
        super().__init__(location_name, description, option_list, npc_list)
        raise NotImplementedError


class Market(Location):
    def __init__(self, location_name, description, option_list, npc_list):
        super().__init__(location_name, description, option_list, npc_list)
        raise NotImplementedError


class RestStop(Location):
    def __init__(self, location_name, description, option_list, npc_list):
        super().__init__(location_name, description, option_list, npc_list)
        raise NotImplementedError


if __name__ == "__main__":
    pass
