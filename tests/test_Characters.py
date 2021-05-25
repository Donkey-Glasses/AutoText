import os
import unittest
from helpers import load_from_data_file
from Characters import *


class TestMonster(unittest.TestCase):
    def setUp(self):
        print(os.getcwd())
        data = load_from_data_file('..\\data\\characters.data')
        male = Gender.from_json(data['Gender']['male'])
        goblin = Species.from_json(data['Species']['goblin'])
        self.goblin = Monster('Smith', 'Gobo', male, goblin, Profession.mob_warrior(), 2)

    def test_monster_general(self):
        self.assertEqual(self.goblin.first_name, 'Gobo')

    def test_monster_stats(self):
        self.assertEqual(self.goblin.agility, 9, f'Agility is {self.goblin.agility} and not 9')

    def test_monster_species(self):
        self.assertEqual(self.goblin.species.mods.agility, 2)
        self.assertEqual(self.goblin.species.mods.intelligence, 0)

    def test_monster_gender(self):
        self.assertEqual(self.goblin.gender.scientific, 'male')


if __name__ == '__main__':
    unittest.main()
