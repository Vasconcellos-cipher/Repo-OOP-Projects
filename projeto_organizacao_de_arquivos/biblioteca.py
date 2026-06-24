class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def listar_livros(self):
        if len(self.livros) == 0:
            print("Nenhum livro cadastrado.")

        else:
            for livro in self.livros:
                livro.mostrar_dados()
                print("===================")

    def listar_usuarios(self):
        if len(self.usuarios) == 0:
            print("Nenhum usuário cadastrado.")

        else:
            for usuario in self.usuarios:
                print(f"Nome: {usuario.nome}")
                print(f"Idade: {usuario.idade}")
                print("===================")

    def emprestar_livro(self, usuario, livro):
        if livro.disponivel:
            livro.disponivel = False
            usuario.livros_emprestados.append(livro)

            print(f"{usuario.nome} pegou '{livro.nome}' emprestado.")

        else:
            print("Livro indisponível.")

    def devolver_livro(self, usuario, livro):
        if livro in usuario.livros_emprestados:
            livro.disponivel = True
            usuario.livros_emprestados.remove(livro)

            print(f"{usuario.nome} devolveu '{livro.nome}'.")

        else:
            print("Este usuário não possui esse livro.")