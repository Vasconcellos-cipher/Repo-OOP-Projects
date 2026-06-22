from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    @abstractmethod
    def trabalhar(self):
        pass


class Programador(Funcionario):
    def __init__(self, nome):
        super().__init__(nome, 5000)

    def trabalhar(self):
        print(f"Programador {self.nome} está codando.")


class Designer(Funcionario):
    def __init__(self, nome):
        super().__init__(nome, 4000)

    def trabalhar(self):
        print(f"Designer {self.nome} está criando layouts.")


class Gerente(Funcionario):
    def __init__(self, nome):
        super().__init__(nome, 7000)

    def trabalhar(self):
        print(f"Gerente {self.nome} está gerenciando a equipe.")


programador = Programador("Ana")
designer = Designer("João")
gerente = Gerente("Maria")

funcionarios = [programador, designer, gerente]

for funcionario in funcionarios:
    funcionario.trabalhar()
    print(f"Salário: R${funcionario.salario}")
    print("====================")