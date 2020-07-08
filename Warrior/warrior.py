class Warrior:
    def __init__(self, name, hp=100, damage=20):
        self.__name = name
        self.__hp = hp
        self.__damage = damage

    # def get_damage(self):
    #     return self.__damage
    #
    # def set_damage(self, value):
    #     if value > 0:
    #         self.__damage = value

    @property
    def name(self):
        return self.__name

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        if value > 0:
            self.__damage = value

    def isAlive(self):
        if self.__hp > 0:
            return True
        else:
            return False

    def __str__(self):
        return f'Name: {self.__name}, HP: {self.__hp}'