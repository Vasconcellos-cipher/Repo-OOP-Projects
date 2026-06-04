class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso!")
            print(f"Saldo atual: R${self.saldo}")
        else:
            print("O valor do depósito deve ser maior que zero!")
    
    def sacar(self, retirar):
        if retirar <= 0:
            print("O valor do saque deve ser maior que zero!")

        elif retirar <= self.saldo:
            self.saldo -= retirar
            print(f"Retirada de R${retirar} realizada com sucesso!")
            print(f"Saldo atual: R${self.saldo}")

        else:
            print("Saldo insuficiente!")
                       
    def mostrar_saldo(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: R${self.saldo}")


conta = Conta("Ana", 5000)

conta.depositar(500)

conta.sacar(1000)

conta.mostrar_saldo()
