from Warrior.warrior import *
import time
import random

def main():
    warrior1 = Warrior("Петр")
    warrior2 = Warrior("Боб", 90, 19)

    while warrior1.isAlive() and warrior2.isAlive():
        k = random.randint(0, 100)
        if k % 2 == 0:
            warrior2.hp -= warrior1.damage
        else:
            warrior1.hp -= warrior2.damage
        print(warrior1)
        print(warrior2)
        time.sleep(1)
    if warrior1.isAlive():
        print("Win", warrior1.name)
    else:
        print("Win", warrior2.name)


main()
