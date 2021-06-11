from unittest import TestCase

import helpers
from Locations import Town


class Test(TestCase):
    def setUp(self) -> None:
        self.save_id = ""
        self.loaded_town = None
        self.town = Town.new_random_town(level_range=10)

    def test_load_from_data_file(self):
        human = helpers.load_from_data_file("species", "species='human'")
        data_dict = {"species": "human", "scientific": "homonus", "adjective": "human", "plural": "humans",
                     "epithet": "jack", "epithet_plural": "jacks"}
        for index, item in enumerate(data_dict.values()):
            self.assertEqual(item, human[index])

    def test_random_from_data(self):
        for i in range(10):
            random_first_name = helpers.random_from_data("first_names", field="name",
                                                         where_clause='gender="male" AND species="goblin"')
            random_last_name = helpers.random_from_data("last_names", field="name",
                                                        where_clause="species='goblin'")
            print(random_first_name + " " + random_last_name)

    def test_save_blob(self):
        self.save_id = helpers.save_blob('TESTTown', self.town)
        print(f'SAVE ID: {self.save_id}')

    def test_load_blob(self):
        self.loaded_town = helpers.load_blob("Test Save File")
        print(self.loaded_town)
