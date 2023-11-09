import numpy as np

class Player:
    PLAYER_1 = 'A'
    PLAYER_2 = 'B'
    NO_PLAYER = 'X'

class GameState:
    magic_square = np.array([[2,7,6],[9,5,1],[4,3,8]])
    def __init__(self):
        self.board = np.full((3, 3), None)
        self.player_to_move = Player.PLAYER_1

    def get_next_player(player):
        if player == Player.PLAYER_1:
            return Player.PLAYER_2
        elif player == Player.PLAYER_2:
            return Player.PLAYER_1
        return Player.NO_PLAYER

    def get_next_state(self, move):
        next_state = GameState()
        next_state.player_to_move = GameState.get_next_player(self.player_to_move)
        next_state.board = np.copy(self.board)
        
        for i in range(3):
            for j in range(3):
                if GameState.magic_square[i][j] == move:
                    next_state.board[i][j] = self.player_to_move

        return next_state

    def minmax(state, move, depth, max_depth):
        print(f"depth: {depth}, {np.ndarray.tolist(state.board)}, {state.player_to_move}")
        if Validator.is_final_state(state) or depth == max_depth:
            return Heuristic.get_score(state), move
        
        next = []
        for next_move in range(1, 10):
            if Validator.is_valid_move(state, next_move):
                next_state = state.get_next_state(next_move)
                next.append(GameState.minmax(next_state, next_move, depth + 1, max_depth))

        f = lambda list: min(next, key=lambda x: x[0])
        if state.player_to_move == Player.PLAYER_1:
            f = lambda list: max(next, key=lambda x: x[0])
        return f(next)

class Validator:
    def check_final_state(state):
        for i in range(3):
            #pe linie
            if all(cell == Player.PLAYER_1 for cell in state.board[i]):
                return True, Player.PLAYER_1
            if all(cell == Player.PLAYER_2 for cell in state.board[i]):
                return True, Player.PLAYER_2
            #pe coloana
            if all(cell == Player.PLAYER_1 for cell in state.board[:,i]):
                return True, Player.PLAYER_1
            if all(cell == Player.PLAYER_2 for cell in state.board[:,i]):
                return True, Player.PLAYER_2
            
        #diag principala
        if all(state.board[i][i] == Player.PLAYER_1 for i in range(3)):
            return True, Player.PLAYER_1
        if all(state.board[i][i] == Player.PLAYER_2 for  i in range(3)):
            return True, Player.PLAYER_2

        #diag secundara
        if all(state.board[i][2-i] == Player.PLAYER_1 for i in range(3)):
            return True, Player.PLAYER_1
        if all(state.board[i][2-i] == Player.PLAYER_2 for i in range(3)):
            return True, Player.PLAYER_2
            
        if None in state.board:
            return False, None
        return True, Player.NO_PLAYER
    
    def is_final_state(state):
        return Validator.check_final_state(state)[0]

    def is_valid_move(state, move):
        for i in range(3):
            for j in range(3):
                if GameState.magic_square[i][j] == move:
                    if state.board[i][j] != None:
                        return False
        return True

class Heuristic:
    def get_score(state):
        SCORES = {
            '3-in-a-line': 100,
            '2-in-a-line': 10,
            '1-in-a-line': 1,
        }
        total_score = 0
        for i in range(3):
            row = state.board[i, :]
            total_score += Heuristic.evaluate_line(row, SCORES)

            col = state.board[:, i]
            total_score += Heuristic.evaluate_line(col, SCORES)

        diagonal1 = np.diagonal(state.board)
        diagonal2 = np.diagonal(np.fliplr(state.board))
        total_score += Heuristic.evaluate_line(diagonal1, SCORES)
        total_score += Heuristic.evaluate_line(diagonal2, SCORES)

        return total_score

    def evaluate_line(line, scores):
        num_player = line.tolist().count(Player.PLAYER_1) #player 1
        num_empty = line.tolist().count(None)
        num_opponent = 3 - num_player - num_empty #player 2

        if num_player == 3:
            return scores['3-in-a-line']
        elif num_player == 2 and num_empty == 1:
            return scores['2-in-a-line']
        elif num_player == 1 and num_empty == 2:
            return scores['1-in-a-line']
        elif num_opponent == 3:
            return -scores['3-in-a-line']
        elif num_opponent == 2 and num_empty == 1:
            return -scores['2-in-a-line']
        elif num_opponent == 1 and num_empty == 2:
            return -scores['1-in-a-line']
        else:
            return 0

# Create a GameState object with a custom board configuration
game_state = GameState()
game_state.board = np.array([
    ['A', 'B', 'B'],
    ['B', 'A', 'A'],
    ['A', 'B', None]
])
game_state.player_to_move = Player.PLAYER_1

# Calculate the heuristic score
heuristic_score = Heuristic.get_score(game_state)
print(f"Heuristic score: {heuristic_score}")

score, move = GameState.minmax(game_state, -1, 0, 4)
print(score, move)