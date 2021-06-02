from unittest import TestCase
from helpers import load_from_data_file


class Test(TestCase):
    def test_load_from_data_file(self):
        human = load_from_data_file("species", "species='human'")
        data_dict = {"species": "human", "scientific": "homonus", "adjective": "human", "plural": "humans",
                     "epithet": "jack", "epithet_plural": "jacks"}
        for index, item in enumerate(data_dict.values()):
            self.assertEqual(item, human[index])
