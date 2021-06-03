import helpers

from typing import Union


class AttributeMods:
    def __init__(self, strength: int, agility: int, constitution: int, intelligence: int, wits: int, willpower: int):
        self.strength = strength
        self.agility = agility
        self.constitution = constitution
        self.intelligence = intelligence
        self.wits = wits
        self.willpower = willpower

    def apply(self, combatant):
        def plus_equal_with_min(c_stat, a_stat, minim: int = 3):
            return max(c_stat + a_stat, minim)

        combatant.strength = plus_equal_with_min(combatant.strength, self.strength)
        combatant.agility = plus_equal_with_min(combatant.agility, self.agility)
        combatant.constitution = plus_equal_with_min(combatant.constitution, self.constitution)
        combatant.intelligence = plus_equal_with_min(combatant.intelligence, self.intelligence)
        combatant.wits = plus_equal_with_min(combatant.wits, self.wits)
        combatant.willpower = plus_equal_with_min(combatant.willpower, self.willpower)

    @classmethod
    def int_list(cls, int_list: Union[tuple, list]):
        stre = int_list[0]
        agil = int_list[1]
        cons = int_list[2]
        inte = int_list[3]
        wits = int_list[4]
        will = int_list[5]
        return AttributeMods(stre, agil, cons, inte, wits, will)

    @classmethod
    def mob_mods(cls):
        return AttributeMods(-3, -3, -3, -3, -3, -3)


class Species:
    def __init__(self, species: str, scientific: str, adjective: str, plural: str, epithet: str, epithet_plural: str,
                 mods: AttributeMods):
        self.species = species
        self.scientific = scientific
        self.adjective = adjective
        self.plural = plural
        self.epithet = epithet
        self.epithet_plural = epithet_plural
        self.mods = mods

    @classmethod
    def from_data(cls, name_string: str):
        data = helpers.load_from_data_file("species", f'species="{name_string}"')
        mod_list = data[6:]
        mods = AttributeMods.int_list(mod_list)
        return Species(data[0], data[1], data[2], data[3], data[4], data[5], mods)

    @classmethod
    def new_game_species(cls):
        species_list = helpers.select_field_from_table('species', 'species')
        option_list = []
        for species in species_list:
            text = species.capitalize()
            selector = species[:1]
            arg = species.lower()
            option_list.append(helpers.Option(text, selector, Species.from_data, arg))
        species_options = helpers.OptionList(option_list)
        new_species = species_options.choose_option()
        return new_species


class Gender:
    def __init__(self, scientific: str, adult: str, diminutive: str, subjective: str, objective: str):
        self.scientific = scientific
        self.adult = adult
        self.diminutive = diminutive
        self.subjective = subjective
        self.objective = objective

    @classmethod
    def from_data(cls, name_string: str):
        data = helpers.load_from_data_file("genders", f'gender="{name_string}"')
        return Gender(data[0], data[1], data[2], data[3], data[4])

    @classmethod
    def new_game_gender(cls):
        gender_list = helpers.select_field_from_table('gender', 'genders', 'WHERE gender!="object"')
        option_list = []
        for gender in gender_list:
            text = gender.capitalize()
            selector = gender[:1]
            arg = gender.lower()
            option_list.append(helpers.Option(text, selector, Gender.from_data, arg))
        gender_options = helpers.OptionList(option_list)
        new_gender = gender_options.choose_option()
        return new_gender


class Profession:
    def __init__(self, profession: str, plural: str, mods: AttributeMods):
        self.profession = profession
        self.plural = plural
        self.mods = mods

    @classmethod
    def warrior(cls):
        return Profession('warrior', 'warriors', AttributeMods.int_list([2, 0, 2, 0, 0, 0]))

    @classmethod
    def mob_warrior(cls):
        return Profession('warrior', 'warriors', AttributeMods.int_list([0, 0, 0, -4, -2, -2]))

    @classmethod
    def from_data(cls, name_string: str):
        data = helpers.load_from_data_file("professions", f'profession="{name_string}"')
        mod_list = data[2:]
        mods = AttributeMods.int_list(mod_list)
        return Profession(data[0], data[1], mods)

    @classmethod
    def new_game_profession(cls):
        profession_list = helpers.select_field_from_table('profession', 'professions', "WHERE mob_only='False'")
        option_list = []
        for prof in profession_list:
            text = prof.capitalize()
            selector = prof[:1]
            arg = prof.lower()
            option_list.append(helpers.Option(text, selector, Profession.from_data, arg))
        profession_list = helpers.OptionList(option_list)
        new_profession = profession_list.choose_option()
        return new_profession


class Character:
    def __init__(self, last_name: str, first_name: str, gender: Gender, species: Species):
        self.last_name = last_name
        self.first_name = first_name
        self.gender = gender
        self.species = species

    def __repr__(self):
        return f'<<{self.__class__.__name__}>> <{id(self)}> Name: {self.last_name} Species: {self.species}'


class NonPlayer(Character):
    def __init__(self, last_name: str, first_name: str, gender: Gender, species: Species,
                 option_list: helpers.OptionList, description: str):
        super().__init__(last_name, first_name, gender, species)
        self.option_list = option_list
        self.description = description

    @classmethod
    def build_with_random_name(cls, species: Species, gender: Gender, option_list, description):
        first, last = generate_random_name(species, gender)
        return NonPlayer(last, first, gender, species, option_list, description)


class Combatant(Character):
    def __init__(self, last_name, first_name: str, gender, species, profession: Profession, level: int = 1):
        super().__init__(last_name, first_name, gender, species)
        self.profession = profession
        self.strength = 10
        self.agility = 10
        self.constitution = 10
        self.intelligence = 10
        self.wits = 10
        self.willpower = 10
        self.hp_per_level = 5
        self.skills = []
        self.level = level
        self.profession.mods.apply(self)
        self.species.mods.apply(self)
        self.missing_hp = 0

    @property
    def max_hp(self):
        return self.level * (self.constitution + self.hp_per_level) + 30

    @property
    def current_hp(self):
        return self.max_hp - self.missing_hp


class Hero(Combatant):
    def __init__(self, last_name, first_name, gender, species, profession, level):
        super().__init__(last_name, first_name, gender, species, profession, level)

    @classmethod
    def new_character(cls):
        level = 1
        species = Species.new_game_species()
        gender = Gender.new_game_gender()
        profession = Profession.new_game_profession()
        first_name = input("What is your character's first name?  >> ")
        last_name = input("What is your character's last name?  >> ")
        return Hero(last_name, first_name, gender, species, profession, level)


class Monster(Combatant):
    def __init__(self, last_name, first_name, gender, species, profession, level):
        super().__init__(last_name, first_name, gender, species, profession, level)
        AttributeMods.mob_mods().apply(self)


def generate_random_name(species, gender):
    first = helpers.random_from_data("first_names", field="name",
                                     where_clause=f'gender="{gender}" AND species="{species}"')
    last = helpers.random_from_data("last_names", field="name", where_clause=f'species={species}')
    return first, last


if __name__ == "__main__":
    pass
