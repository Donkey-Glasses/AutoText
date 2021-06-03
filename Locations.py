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


class Theme:
    def __init__(self, theme_name: str):
        self.theme_name = theme_name
        self.noun_list = []
        self.adjective_list = []
        self.populate_lists()

    def __repr__(self):
        return f'<<{id(self)}>> <<{self.__class__.__name__}>> Name: {self.theme_name}'

    def populate_lists(self):
        noun_fields = ['noun1', 'noun2', 'noun3']
        self.noun_list.extend(helpers.field_list_from_table(noun_fields, 'dungeon_themes',
                                                            where_string=f'WHERE name="{self.theme_name}"'))
        adjective_fields = ['adjective1', 'adjective2', 'adjective3']
        self.adjective_list.extend(helpers.field_list_from_table(adjective_fields, 'dungeon_themes',
                                                                 where_string=f'WHERE name="{self.theme_name}"'))

    @classmethod
    def random_theme(cls):
        name = helpers.random_from_data('dungeon_themes', 'name', first_only=True)
        return Theme(name)


class Dungeon(Location):
    def __init__(self, location_name, description, option_list, npc_list, theme):
        super().__init__(location_name, description, option_list, npc_list)

    @classmethod
    def random_dungeon(cls):
        theme = Theme.random_theme()
        options = OptionList.dungeon()
        npcs = list()
        location_name = "Pants"
        description = "PLACEHOLDER"
        return Dungeon(location_name, description, options, npcs, theme)


class Market(Location):
    def __init__(self, location_name, description, option_list, npc_list):
        super().__init__(location_name, description, option_list, npc_list)

    @classmethod
    def random_market(cls, town_name: str):
        return Market(f'{town_name} Market', "A market!", OptionList.market(), list())


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

    def __repr__(self):
        return f'<<{id(self)}>> <<{self.__class__.__name__}>> Name: {self.town_name}, species: {self.common_race}, ' \
               f'level: {self.level_range}'

    @classmethod
    def new_random_town(cls, level_range: int):
        def town_name(race: str) -> str:
            first_type, first_value = helpers.random_from_data_weighted('town_names', 'type, value', 'type!="suffix"')
            if first_type == 'species':
                if first_value == 'species':  # avoids unnecessary DB access
                    first_value = race
                else:
                    first_value = helpers.select_field_from_table(field=first_value, table='species',
                                                                  where_string=f'WHERE species="{race}"')[0]
            second = helpers.random_from_data_weighted('town_names', 'value', 'type="suffix"')[0]
            return first_value.capitalize() + second
        common_race = helpers.random_from_data_weighted('species', 'species')[0]
        name = town_name(common_race)
        rest_stop = RestStop.random_rest_stop()
        market = Market.random_market(name)
        dungeon = Dungeon.random_dungeon()
        return Town(name, rest_stop, market, dungeon, level_range, common_race)


if __name__ == "__main__":
    pass
