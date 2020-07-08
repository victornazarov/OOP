class Money:
    def __init__(self, rubles=0, penny=0):
        self.__rubles = rubles
        self.__penny = penny

    def __str__(self):
        return f"{self.__rubles}r. {self.__penny}cop."

    def __repr__(self):
        return f"{self.__rubles}r. {self.__penny}cop."

    def __add__(self, money):
        trubles = self.__rubles + money.__rubles
        tpenny = self.__penny + money.__penny
        if tpenny >= 100:
            tpenny -= 100
            trubles += 1
        return Money(trubles, tpenny)

    def __lt__(self, money):
        balance1 = self.__rubles * 100 + self.__penny
        balance2 = money.__rubles * 100 + money.__penny
        if balance1 < balance2:
            return True
        else:
            return False
