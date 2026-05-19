class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome

        if preco >= 0:
            self.__preco = preco
        else:
            self.__preco = 0
            print("Preço inválido!")

    def alterar_preco(self, novo_preco):
        if novo_preco >= 0:
            self.__preco = novo_preco
        else:
            print("Preço inválido!")
            
    def mostrar_preco(self):
        print(f"O produto {self.__nome} tem o valor de {self.__preco}")
            
produto1 = Produto("Mouse", -100)
produto1 = Produto("Mouse", 200)
produto1.mostrar_preco()