class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** 0.5

    # LÓGICA DO RETÂNGULO: Usa apenas 1 caractere para não distorcer a proporção
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = ""
        for _ in range(self.height):
            picture += " # " * self.width + "\n"
        return picture

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height
    
    # LÓGICA DO QUADRADO: Duplica o caractere ("##") para o terminal não deixar ele "magro"
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = ""
        
        for _ in range(self.height):
            picture += " # " * self.width + "\n"
        return picture
        

    def __str__(self):
        return f"Square(side={self.width})"


# --- CÓDIGO DE EXECUÇÃO ---
while True:
    try:
        opcao = input("Digite R para Retângulo ou Q para Quadrado: ").upper()

        if opcao == "R":
            width = int(input("Largura: "))
            height = int(input("Altura: "))

            if width == height:
                print("\nLargura e altura são iguais.")
                print("Isso é um Quadrado. Criando um Quadrado automaticamente...\n")
                forma = Square(width)
            else:
                forma = Rectangle(width, height)

        elif opcao == "Q":
            side = int(input("Lado: "))
            forma = Square(side)

        else:
            print("Opção inválida!")
            continue

        print("\nResultado:")
        print(forma)
        print("Área:", forma.get_area())
        print("Perímetro:", forma.get_perimeter())
        print(f"Diagonal: {forma.get_diagonal():.2f}")

        print("\nDesenho:")
        print(forma.get_picture())

        break

    except ValueError:
        print("Digite apenas números inteiros!")