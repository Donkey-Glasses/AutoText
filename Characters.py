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

        plus_equal_with_min(combatant.strength, self.strength)
        plus_equal_with_min(combatant.agility, self.agility)
        plus_equal_with_min(combatant.constitution, self.constitution)
        plus_equal_with_min(combatant.intelligence, self.intelligence)
        plus_equal_with_min(combatant.wits, self.wits)
        plus_equal_with_min(combatant.willpower, self.willpower)

    @classmethod
    def int_list(cls, int_list: list):
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
    def human(cls):
        return Species('human', 'homonus', 'human', 'humans', 'jack', 'jacks',
                       AttributeMods.int_list([1, 1, 1, 1, 1, 1]))

    @classmethod
    def elf(cls):
        return Species('elf', 'elvynus', 'elven', 'elves', 'ear', 'ears',
                       AttributeMods.int_list([0, 2, 0, 2, 0, 0]))

    @classmethod
    def dwarf(cls):
        return Species('dwarf', 'dwarvus', 'dwarven', 'dwarves', 'dung', 'dungs',
                       AttributeMods.int_list([2, 0, 2, 0, 0, 0]))

    @classmethod
    def goblin(cls):
        return Species('goblin', 'gobican', 'goblin', 'goblins', 'gib', 'gibs',
                       AttributeMods.int_list([0, 2, 0, 0, 0, 0]))


class Gender:
    def __init__(self, scientific: str, adult: str, diminutive: str, subjective: str, objective: str):
        self.scientific = scientific
        self.adult = adult
        self.diminutive = diminutive
        self.subjective = subjective
        self.objective = objective

    @classmethod
    def non_binary(cls):
        return Gender('non-binary', 'non-binary', 'enby', 'they', 'them')

    @classmethod
    def female(cls):
        return Gender('female', 'woman', 'girl', 'she', 'her')

    @classmethod
    def male(cls):
        return Gender('male', 'man', 'boy', 'he', 'him')

    @classmethod
    def object(cls):
        return Gender('object', 'object', 'object', 'it', 'it')


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


class Character:
    def __init__(self, name: str, gender: Gender, species: Species):
        self.name = name
        self.gender = gender
        self.species = species


class Combatant(Character):
    def __init__(self, name, gender, species, profession: Profession, level: int = 1):
        super().__init__(name, gender, species)
        self.profession = profession
        self.strength = 10
        self.agility = 10
        self.constitution = 10
        self.intelligence = 10
        self.wits = 10
        self.willpower = 10
        self.skills = []
        self.level = level
        self.profession.mods.apply(self)
        self.species.mods.apply(self)


class Player(Combatant):
    def __init__(self, name, gender, species, profession, level):
        super().__init__(name, gender, species, profession, level)


class Monster(Combatant):
    raise NotImplementedError


class NonPlayer(Character):
    raise NotImplementedError
