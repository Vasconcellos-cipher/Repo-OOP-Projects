class Animal:
    def __init__(self):
        self.move = 0  

class Peixe(Animal):
    def mover(self):
        self.move += 1  
        print(f"Peixe nadou! Posição acumulada: {self.move}")

class Passaro(Animal):
    def mover(self):
        self.move += 3  
        print(f"Pássaro voou! Posição acumulada: {self.move}")

class Cachorro(Animal):
    def mover(self):
        self.move += 2  
        print(f"Cachorro correu! Posição acumulada: {self.move}")
        
animais = [Peixe(), Passaro(), Cachorro()]

animais = [Peixe(), Passaro(), Cachorro()]

print("--- PRIMEIRA RODADA ---")
for animal in animais:
    animal.mover()

print("\n--- SEGUNDA RODADA (Valores gravados!) ---")
for animal in animais:
    animal.mover()

print("\n--- TERCEIRA RODADA (Acumulando mais!) ---")
for animal in animais:
    animal.mover()
