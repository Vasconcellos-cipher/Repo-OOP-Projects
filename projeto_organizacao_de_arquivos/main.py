from livro import Livro
<<<<<<< HEAD
from usuario import Usuario
from biblioteca import Biblioteca


biblioteca = Biblioteca()


usuario1 = Usuario("Carlos", 25)

=======
>>>>>>> 26d5e4eba81f3528322b2d4d85f49f8a923d28b6

livro1 = Livro(
    "Python para Iniciantes",
    "Ana Souza",
    2026,
    "Tecnologia"
)

<<<<<<< HEAD
livro2 = Livro(
    "Linux para Iniciantes",
    "João Silva",
    2025,
    "Tecnologia"
)


biblioteca.adicionar_usuario(usuario1)

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)


print("===== LIVROS DA BIBLIOTECA =====")
biblioteca.listar_livros()


print("\n===== EMPRÉSTIMO =====")
biblioteca.emprestar_livro(usuario1, livro1)


print("\n===== LIVROS EMPRESTADOS =====")
usuario1.mostrar_livros_emprestados()


print("\n===== DEVOLUÇÃO =====")
biblioteca.devolver_livro(usuario1, livro1)


print("\n===== LIVROS DA BIBLIOTECA =====")
biblioteca.listar_livros()
=======
livro1.mostrar_dados()
>>>>>>> 26d5e4eba81f3528322b2d4d85f49f8a923d28b6
