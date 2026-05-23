class Conta:
    def __init__(self, titular, saldo_privado):
        self.__titular = titular
        self._saldo_privado = saldo_privado

    def depositar(self, valor):
        if valor > 0:
            self._saldo_privado += valor
            print(f"Depósito de R${valor} realizado com sucesso!")
        else:
            print("Valor inválido!")

    def sacar(self, retirada):
        if retirada <= self._saldo_privado:
            self._saldo_privado -= retirada
            print(f"Retirada de R${retirada} realizada com sucesso!")
        else:
            print("Saldo insuficiente!")

    def mostrar_saldo(self):
        print(f"Saldo atual: R${self._saldo_privado}")


class ContaPoupanca(Conta):
    def __init__(self, titular, saldo_privado, rendimento):
        super().__init__(titular, saldo_privado)

        if rendimento > 0:
            self.rendimento = rendimento
        else:
            self.rendimento = 0
            print("Rendimento inválido! Definido como 0.")

    def aplicar_rendimento(self):
        self._saldo_privado += self.rendimento

        print(f"Rendimento de R${self.rendimento} aplicado!")


conta1 = Conta("Ana", 1000)

conta1.depositar(500)
conta1.sacar(200)
conta1.mostrar_saldo()


print("\n====================\n")


poupanca = ContaPoupanca("Carlos", 2000, -300)

poupanca.aplicar_rendimento()

poupanca.mostrar_saldo()