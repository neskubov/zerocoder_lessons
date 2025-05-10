class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other_hero):
        other_hero.health = other_hero.health - self.attack_power
        print(f"{self.name} атаковал {other_hero.name} и нанес урон: {self.attack_power}.\n",
              f"Здоровье {other_hero.name}: {other_hero.health}")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        while True:
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.player.name} победил!")
                break
            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.computer.name} победил!")
                break

player = Hero("player")
computer = Hero("computer")
Game(player, computer).start()
