class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
<<<<<<< HEAD
        self.livros_emprestados = []

    def mostrar_livros_emprestados(self):
        if len(self.livros_emprestados) == 0:
            print("Nenhum livro emprestado.")

        else:
            for livro in self.livros_emprestados:
                livro.mostrar_dados()
                print("===================")
=======
        self.livros_emprestados = []
>>>>>>> 26d5e4eba81f3528322b2d4d85f49f8a923d28b6
