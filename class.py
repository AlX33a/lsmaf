from unicodedata import name


class Animal:
    def __init__(self, name, size, type):
        self.name = name
        self.size = size
        self.type = type

    def move(self):
        print(self.name, 'moving')


class Cat(Animal):
    say = 'meow'

    def __init__(self, name, size, type, color):
        super().__init__(name, size, type)
        self.color = color

    def move(self):
        # super().move()
        print(self.name, 'walking')

class Lion(Cat):
    say = 'raaaarw'

    def __init__(self, name, size, type, color, pride):
        super().__init__(name, size, type, color)
        self.pride = pride

    def attack(self, target):
        print(self.name, 'attack', target.name)


# cat = Animal(name = 'alica',size = 'small',type = 'predator')
# print(cat.name)
# cat.move()

alice = Cat(color = 'white', name = 'alica', size = 'small', type = 'predator')
print(alice.size)
print(alice.color)
alice.move()

simba = Lion(color = 'yellow', name = 'simba', size = 'large', type = 'predator', pride = 'main')
simba.move()
simba.attack(alice)