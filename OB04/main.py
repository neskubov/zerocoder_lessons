from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def __init__(self, name="Меч", damage=1):
        self.name = name
        self.damage = damage

    def attack(self):
        print("Боец наносит удар мечом.")

class Bow(Weapon):
    def __init__(self, name="Лук", damage=1):
        self.name = name
        self.damage = damage

    def attack(self):
        print("Боец наносит удар из лука.")

class Monster():
    def __init__(self, health=1):
        self.health = health

class Fighter():
    def __init__(self, weapon=''):
        self.weapon = weapon

    def change_weapon(self, weapon):
        self.weapon = weapon
        print(f"Боец выбирает {self.weapon.name}.")

    def attack(self, monster):
        self.weapon.attack()
        if monster.health - self.weapon.damage == 0:
            print("Монстр побежден!")


ivan = Fighter()
ivan.change_weapon(Sword())
ivan.attack(Monster())
ivan.change_weapon(Bow())
ivan.attack(Monster())