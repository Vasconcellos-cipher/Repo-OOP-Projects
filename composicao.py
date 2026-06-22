''' 
Composição é quando uma classe "TEM UM" objeto de outra classe, e não o que "É UM", pertence a classe.
'''

class Motor:
    def __init__(self, potencia):
        self.potencia = potencia


class Carro:
    def __init__(self, marca, motor):
        self.marca = marca
        self.motor = motor

    def mostrar_dados(self):
        print(f"Marca: {self.marca}")
        print(f"Potência: {self.motor.potencia}")


motor1 = Motor("150cv")

carro1 = Carro("Toyota", motor1)

carro1.mostrar_dados()