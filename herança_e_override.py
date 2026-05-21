class Animal:
    def fazer_som(self):
        print("Som genérico")


class Cachorro(Animal):
    def fazer_som(self):
        print("Au au")


class Gato(Animal):
    def fazer_som(self):
        print("Miau")
    
animal = Cachorro()
animal.fazer_som()

animal2 = Gato()
animal2.fazer_som()