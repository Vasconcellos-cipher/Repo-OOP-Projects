from abc import ABC, abstractmethod

class Funcionario(ABC):
    @abstractmethod
    def trabalhar(self):
        pass
    
class Programador(Funcionario):
    def trabalhar(self):
        print("Programador está codando.")
        
class Designer(Funcionario):
    def trabalhar(self):
        print("Designer está criando layout.")
        
        
programador = Programador()
designer = Designer()

programador.trabalhar()
designer.trabalhar()