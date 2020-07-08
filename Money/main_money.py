from Money.money import *
import random

moneyList = list()

for i in range(10):
    b = Money(random.randint(0, 99), random.randint(0, 99))
    moneyList.append(b)
print("Изначальный:")
print(moneyList)
# for money in moneyList:
#     print(money)
moneyList.sort()
print("Отсортированный:")
for money in moneyList:
    print(money)


