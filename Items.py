

class Equipment:
    def __init__(self):
        raise NotImplementedError


class Weapon(Equipment):
    def __init__(self):
        super().__init__()
        raise NotImplementedError


class Armor(Equipment):
    def __init__(self):
        super().__init__()
        raise NotImplementedError


class Consumable:
    def __init__(self):
        raise NotImplementedError


class Potion(Consumable):
    def __init__(self):
        super().__init__()
        raise NotImplementedError


if __name__ == "__main__":
    pass
