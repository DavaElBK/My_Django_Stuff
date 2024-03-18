class Animal():

    def __init__(self) -> None:
        print('Animal Created')
    def whoAmI(self):
        print('Animal')
    def eat(self):
        print('eating')
  
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('dog created')

mydog=Dog()
mydog.whoAmI()
mydog.eat()