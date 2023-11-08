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
    
    def minmax(state, depth, max_depth):
        if Validator.is_final_state(state) or depth == max_depth:
            return Heuristic.get_score(state), state
        #TODO
        

class Validator:
    def is_final_state(state):
        if None in state.board:
            return False, None
        for i in range(3):
            if all(cell == Player.PLAYER_1 or cell == Player.PLAYER_2 for cell in state.board[i]):
                return True, state.board[i][0]
            if all(cell == Player.PLAYER_1 or cell == Player.PLAYER_2 for cell in state.board[:,i:i+1]):
                return True, state.board[0][i]
        
        if all(state.board[i][i] == Player.PLAYER_1 or state.board[i][i] == Player.PLAYER_2 for i in range(3)):
            return True, state.board[0][0]
        if all(state.board[i][2-i] == Player.PLAYER_1 or state.board[i][2-i] == Player.PLAYER_2 for i in range(3)):
            return True, state.board[0][2]
        
        return True, Player.NO_PLAYER
    
    def is_valid_move(state, move):
        for i in range(3):
            for j in range(3):
                if GameState.magic_square[i][j] == move:
                    if state.board[i][j] != None:
                        return False
        return True

class Heuristic:
    @staticmethod
    def get_score(state):
        # Define the scoring values
        SCORES = {
            '3-in-a-line': 100,
            '2-in-a-line': 10,
            '1-in-a-line': 1,
        }

        # Initialize the total score
        total_score = 0

        # Check each of the 8 lines (3 rows, 3 columns, and 2 diagonals)
        for i in range(3):
            # Check rows
            row = state.board[i, :]
            total_score += Heuristic.evaluate_line(row, SCORES)

            # Check columns
            col = state.board[:, i]
            total_score += Heuristic.evaluate_line(col, SCORES)

        # Check diagonals
        diagonal1 = np.diagonal(state.board)
        diagonal2 = np.diagonal(np.fliplr(state.board))
        total_score += Heuristic.evaluate_line(diagonal1, SCORES)
        print(total_score)
        total_score += Heuristic.evaluate_line(diagonal2, SCORES)
        print(total_score)

        return total_score

    @staticmethod
    def evaluate_line(line, scores):
        # Evaluate a single line
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
    ['A', None, 'B'],
    [None, None, 'B'],
    ['A', None, None]
])

# Calculate the heuristic score
heuristic_score = Heuristic.get_score(game_state)
print(f"Heuristic score: {heuristic_score}")