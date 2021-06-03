import helpers

from helpers import Option, OptionList
from typing import List
from random import randint


class Location:
    def __init__(self, location_name: str, description: str, option_list: OptionList, npc_list: List):
        self.location_name = location_name
        self.description = description
        self.option_list = option_list
        self.npc_list = npc_list

    def on_enter(self):
        print(self.location_name.center(40, '*'))
        print(self.description)
        print('-' * 40)
        if len(self.npc_list) > 0:
            for npc in self.npc_list:
                print(f'  {npc.last_name}')
                print(f'  {npc.description}')
        self.option_list.choose_option()


class Dungeon(Location):
    def __init__(self, location_name, description, option_list, npc_list):
        super().__init__(location_name, description, option_list, npc_list)
        raise NotImplementedError

    @classmethod
    def random_dungeon(cls):
        raise NotImplementedError


class Market(Location):
    def __init__(self, location_name, description, option_list, npc_list):
        super().__init__(location_name, description, option_list, npc_list)

    @classmethod
    def random_market(cls, town_name: str):
        raise NotImplementedError


class RestStop(Location):
    def __init__(self, location_name, description, option_list, npc_list):
        super().__init__(location_name, description, option_list, npc_list)

    @classmethod
    def random_rest_stop(cls):
        def random_name() -> str:
            first_type, first_value = helpers.random_from_data(table="inn_names", field="*", first_only=False)
            second_value = helpers.random_from_data(table="inn_names", field="value", where_clause="type='noun'")
            if first_type == 'noun':
                return f"The {first_value} and {second_value}"
            elif first_type == 'adjective':
                return f"The {first_value} {second_value}"

        name = random_name()
        description = "An INN. ADD TEXT LATER DAWG."
        options = helpers.OptionList.rest_stop()
        npc_list = []
        return RestStop(name, description, options, npc_list)


class Town:
    def __init__(self, town_name: str, rest_stop: RestStop, market: Market, dungeon: Dungeon,
                 level_range: int, common_race: str):
        self.town_name = town_name
        self.common_race = common_race
        self.rest_stop = rest_stop
        self.market = market
        self.dungeon = dungeon
        self.level_range = level_range

    @classmethod
    def new_random_town(cls, level_range: int):
        def town_name(race: str) -> str:
            first_type, first_value = helpers.random_from_data_weighted('town_names', 'type, value', 'type!="suffix"')
            if first_type == 'species':
                first_value = helpers.select_field_from_table(field=first_value, table='species',
                                                              where_string=f'WHERE species={race}')
            second = helpers.random_from_data_weighted('town_names', 'value', 'type="suffix"')[0]
            return first_value + second
        common_race = helpers.random_from_data_weighted('species', 'species')
        name = town_name(common_race)
        rest_stop = RestStop.random_rest_stop()
        market = Market.random_market()
        dungeon = Dungeon.random_dungeon()
        return Town(name, rest_stop, market, dungeon, level_range, common_race)


if __name__ == "__main__":
    pass
