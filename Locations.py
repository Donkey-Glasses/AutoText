from typing import List

from main import OptionList
from Characters import Hero, NonPlayer


class Location:
    def __init__(self, location_name: str, description: str, option_list: OptionList, npc_list: List[NonPlayer]):
        self.location_name = location_name
        self.description = description
        self.option_list = option_list
        self.npc_list = npc_list

    def on_enter(self, player: Hero):
        print(self.location_name.center(40, '*'))
        print(self.description)
        print('-' * 40)
        for npc in self.npc_list:
            print(f'  {npc.name}')
            print(f'  {npc.description}')


class Dungeon(Location):
    raise NotImplementedError


class Market(Location):
    raise NotImplementedError


class RestStop(Location):
    raise NotImplementedError


start = Location()
