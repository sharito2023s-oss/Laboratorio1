from collections import deque
from PuzzleState import PuzzleState

class PuzzleSolver:
    @staticmethod
    def bfs(initial_state, goal_state):
        visited = set()
        queue = deque([initial_state])
        
        while queue:
            current_state = queue.popleft()
            
            if current_state.is_goal(goal_state):
                return PuzzleSolver.reconstruct_path(current_state)
            
            if current_state not in visited:
                visited.add(current_state)
                for move in current_state.get_possible_moves():
                    if move not in visited:
                        queue.append(move)
        
        return None
    
    @staticmethod
    def reconstruct_path(state):
        path = []
        while state.parent is not None:
            path.append((state.move, state.board))
            state = state.parent
        path.reverse()
        return path