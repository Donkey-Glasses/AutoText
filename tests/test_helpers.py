from unittest import TestCase

import helpers
from helpers import load_from_data_file


class Test(TestCase):
    def test_load_from_data_file(self):
        human = load_from_data_file("species", "species='human'")
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
