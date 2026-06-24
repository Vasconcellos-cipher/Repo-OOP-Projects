class Livro:
    def __init__(self, nome, autor, ano, genero):
        self.nome = nome
        self.autor = autor
        self.ano = ano
        self.genero = genero
        self.disponivel = True
<<<<<<< HEAD

=======
        
>>>>>>> 26d5e4eba81f3528322b2d4d85f49f8a923d28b6
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Autor: {self.autor}")
        print(f"Ano: {self.ano}")
        print(f"Gênero: {self.genero}")
        print(f"Disponível: {self.disponivel}")