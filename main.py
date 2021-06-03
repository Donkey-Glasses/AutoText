import Locations
import Characters
import helpers
import Items
import Combat

from json import load


class Game:
    def __init__(self):
        self.hero = None
        self.town = None
        self.game_options = None
        self.read_options("data\\default.options")
        new_game_option = helpers.Option('New Game', 'n', self.new_game)
        load_game_option = helpers.Option('Load Game', 'l', self.load_game)
        start_options = helpers.OptionList([new_game_option, load_game_option])
        self.location = Locations.Location("WELCOME TO AUTOTEXT", "Welcome to AutoText!", start_options, [])
        self.location.on_enter()

    def read_options(self, options_file: str):
        with open(options_file) as options:
            self.game_options = load(options)

    def new_game(self):
        """
        def __init__(self, last_name, first_name, gender, species, profession, level,
                     location: Locations.Location):
            super().__init__(last_name, first_name, gender, species, profession, level)
            self.location = location
        """
        self.hero = Characters.Hero.new_character()
        self.town = Locations.Town.new_random_town(5)
        self.change_location(self.town.rest_stop)

    def load_game(self):
        raise NotImplementedError

    def change_location(self, location: Locations.Location):
        self.location = location
        self.location.on_enter()


if __name__ == '__main__':
    main = Game()
