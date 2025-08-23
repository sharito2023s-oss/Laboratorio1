from PuzzleState import PuzzleState
from PuzzleSolver import PuzzleSolver

class PuzzleGame:
    def __init__(self, initial_board, goal_board):
        self.initial_state = PuzzleState(initial_board)
        self.goal_state = PuzzleState(goal_board)
    
    def solve(self):
        solution = PuzzleSolver.bfs(self.initial_state, self.goal_state)
        if solution:
            print("Solución encontrada en {} pasos:".format(len(solution)))
            print("Estado inicial:")
            print(self.initial_state)
            print()
            
            for step, (move, board) in enumerate(solution, 1):
                print("Paso {}: Mover {}".format(step, move))
                print('\n'.join([' '.join(map(str, row)) for row in board]))
                print()
        else:
            print("No se encontró solución.")

# Ejemplo de uso (esto es lo que faltaba para que se muestre algo)
initial_board = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]

goal_board = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

game = PuzzleGame(initial_board, goal_board)
game.solve()