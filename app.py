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
    
    
        
            