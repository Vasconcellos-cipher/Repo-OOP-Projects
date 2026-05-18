class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def mostrar_saldo(self):
        print(f"Saldo atual: R${self.saldo}")
        
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso!") 
            
    def sacar(self, retirar):
        if retirar <= self.saldo:
            self.saldo -= retirar
            print(f"Retirada de R${retirar} realizada com sucesso!")
        else:
            print("Saldo insuficiente!")
  
conta = ContaBancaria("Ana", 5000)  
conta.depositar(500)
conta.mostrar_saldo()
conta.sacar(60000)
conta.mostrar_saldo()