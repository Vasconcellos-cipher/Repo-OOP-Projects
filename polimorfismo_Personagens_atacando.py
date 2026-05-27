class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, alvo):
        print(f"{self.nome} fez um ataque genérico!")
            
    def tomar_dano(self, dano):
        self.vida -= dano
        
class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 150, 20)
        
    def atacar(self):
        print(f"{self.nome} usou espada pesada!")

class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 120, 40)
        
    def atacar(self):
        print(f"{self.nome} lançou bola de fogo!")

class Arqueiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 100, 50)
        
    def atacar(self):
        print(f"{self.nome} disparou flecha crítica!")
        
guerreiro = Guerreiro("Thorin")

mago = Mago("Merlin")

arqueiro = Arqueiro("Legolas")
        
personagens = [guerreiro, mago, arqueiro]
for personagem in personagens:
    personagem.atacar()
    print("=========================\n")
    

