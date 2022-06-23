# class Asd:
#     my_arg = 'test arg'
#     @classmethod
#     def asdf(cls):
#         print(cls.my_arg)


# print(Asd.my_arg)
# Asd.asdf()

#'cat name: ' + self.name + '\ncat color: '+ self.color + '\n cat age: ' + self.age

class Cat:
    
    say = 'meow'

    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

#как выводить, если просят отображение в итерабельных объектах   
    def __repr__(self):
        return self.name

#как выводить если просят строчное отображение
    def __str__(self):
        return self.name
    
    def say_your_name(self):
        print('my name is ', self.name, '', self.__class__.say, '!')

    @classmethod
    def walk(cls):
        print('cats walks')

    @classmethod
    def let_say(cls):
        print(cls.say) #cars^)

cats = []
alice = Cat('alice', 'white','2')
# cats.append(alice)
# gja = Cat('gja', 'black', '1000')
# cats.append(gja)

# print(cats)
# print(cats[0])
# print(cats[0].color)
# cats[0].color = 'orange'
# print(cats[0].color)

# cats[0].say_your_name()
# cats[-1].say_your_name()
print(type(Cat))
print(type(alice))