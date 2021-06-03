from unittest import TestCase
import Locations


class TestTheme(TestCase):
    def test_populate_lists(self):
        names = ['crypt', 'swamp']
        for name in names:
            new_theme = Locations.Theme(theme_name=name)
            new_theme.populate_lists()
            print(new_theme)


class TestTown(TestCase):
    def test_new_random_town(self):
        for i in range(0, 1000, 10):
            new_location = Locations.Town.new_random_town(i)
            print(new_location)
