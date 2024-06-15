class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au!! Au!!"

class Gato(Animal):
    def falar(self):
        return "Miau!!!!!"

def som(animal):
    print(animal.falar())

rex = Cachorro()
felix = Gato()

som(rex)
som(felix)
