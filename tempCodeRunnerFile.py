if all(state.board[i][i] == Player.PLAYER_1 or state.board[i][i] == Player.PLAYER_2 for i in range(3)):
            return True, state.board[0][0]