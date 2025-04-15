from data_base import *

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

class Bird(Animal):
    def __init__(self, name="Bird", age=1):
        super().__init__(name, age)
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"Чирик")

class Mammal(Animal):
    def __init__(self, name="Mammal", age=1):
        super().__init__(name, age)
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"Му")

class Reptile(Animal):
    def __init__(self, name="Reptile", age=1):
        super().__init__(name, age)
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"Ща")

class ZooKeeper:
    def __init__(self, name="ZooKeeper"):
        self.name = name

    def feed_animal(self, animal):
        print(f"Покормил {animal}")

class Veterinarian:
    def __init__(self, name="Veterinarian"):
        self.name = name

    def heal_animal(self, animal):
        print(f"Полечил {animal}")

class Zoo:
    def __init__(self, data_base):
        self.list_employees = set(data_base["list_employees"])
        self.list_animals = set(data_base["list_animals"])

    def add_animal(self, animal):
        self.list_animals.add(animal)

    def add_employer(self, employer):
        self.list_employees.add(employer)

    def get_list_animals(self):
        print(f"Список животных {self.list_animals}")

    def get_list_employees(self):
        print(f"Список сотрудников {self.list_employees}")

    def save_data(self):
        data_base = {}
        data_base["list_employees"] = list(set(self.list_employees))
        data_base["list_animals"] = list(set(self.list_animals))
        save_list_zoo(data_base)

def animal_sound(list_animals):
    for animal in list_animals:
        animal.make_sound()


bird = Bird()
mammal = Mammal()
reptile = Reptile()

animals = [bird, mammal, reptile]
animal_sound(animals)

data_base = load_list_zoo()

zoo = Zoo(data_base)

zoo.add_animal(bird.name)
zoo.add_animal(mammal.name)
zoo.add_animal(reptile.name)

zookeeper = ZooKeeper()
zoo.add_employer(zookeeper.name)

zoo.get_list_animals()
zoo.get_list_employees()

zoo.save_data()


