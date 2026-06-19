import abc
import random

class Player(abc.ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        if not self.moves:
            return self.position
            
        selected_move = random.choice(self.moves)

        # Corrigido de self.y para y (variável local) para manter a consistência
        x = self.position[0] + selected_move[0]
        y = self.position[1] + selected_move[1]
        self.position = (x, y)

        self.path.append(self.position)
        return self.position

    @abc.abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        # Movimentos ortogonais (cima, baixo, esquerda, direita)
        self.moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def level_up(self):
        # Adiciona movimentos diagonais ao subir de nível
        diagonal_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.moves.extend(diagonal_moves)
        print("▲ Pawn subiu de nível! Agora ele pode se mover nas diagonais.")


# --- Exemplo de Execução/Simulação ---
if __name__ == "__main__":
    print("--- Criando o Pawn ---")
    pawn = Pawn()
    print(f"Posição inicial: {pawn.position}")
    print(f"Movimentos possíveis: {pawn.moves}\n")

    print("--- Fazendo 3 movimentos normais ---")
    for _ in range(3):
        pawn.make_move()
        print(f"Moveu para: {pawn.position}")

    print("\n--- Subindo de Nível ---")
    pawn.level_up()
    print(f"Novos movimentos possíveis: {pawn.moves}\n")

    print("--- Fazendo mais 3 movimentos (com diagonais inclusas) ---")
    for _ in range(3):
        pawn.make_move()
        print(f"Moveu para: {pawn.position}")

    print(f"\nHistórico completo do caminho percorrido:\n{pawn.path}")