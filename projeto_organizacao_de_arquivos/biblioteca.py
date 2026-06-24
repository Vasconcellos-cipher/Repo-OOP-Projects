class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        
    def adicionar_livro(self, livro):
        self.livros.append(livro)
        
        
    def mostrar_livros(self):
        if len(self.livros) == 0:
            print("Nenhum livro cadastrado.")

        else:
            for livro in self.livros:
                livro.mostrar_dados()
                print("===================")