class PuzzleState:
    def __init__(self, board, parent=None, move=None, depth=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        self.blank_pos = self.find_blank()
    
    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)
        return None
    
    def is_goal(self, goal_state):
        return self.board == goal_state.board
    
    def get_possible_moves(self):
        moves = []
        i, j = self.blank_pos
        
        if i > 0:  # Arriba
            new_board = [row[:] for row in self.board]
            new_board[i][j], new_board[i-1][j] = new_board[i-1][j], new_board[i][j]
            moves.append(PuzzleState(new_board, self, 'up', self.depth + 1))
        
        if i < 2:  # Abajo
            new_board = [row[:] for row in self.board]
            new_board[i][j], new_board[i+1][j] = new_board[i+1][j], new_board[i][j]
            moves.append(PuzzleState(new_board, self, 'down', self.depth + 1))
        
        if j > 0:  # Izquierda
            new_board = [row[:] for row in self.board]
            new_board[i][j], new_board[i][j-1] = new_board[i][j-1], new_board[i][j]
            moves.append(PuzzleState(new_board, self, 'left', self.depth + 1))
        
        if j < 2:  # Derecha
            new_board = [row[:] for row in self.board]
            new_board[i][j], new_board[i][j+1] = new_board[i][j+1], new_board[i][j]
            moves.append(PuzzleState(new_board, self, 'right', self.depth + 1))
        
        return moves
    
    def __eq__(self, other):
        return self.board == other.board
    
    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.board))
    
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.board])