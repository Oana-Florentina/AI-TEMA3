import numpy as np

class Player:
    PLAYER_1 = 'A'
    PLAYER_2 = 'B'
    NO_PLAYER = 'X'

class GameState:
    def __init__(self):
        self.board = np.full((3, 3), None)
        self.magic_square = np.array([[2,7,6],[9,5,1],[4,3,8]])
        self.player_to_move = Player.PLAYER_1


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
        
            