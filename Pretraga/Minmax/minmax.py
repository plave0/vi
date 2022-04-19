import copy

class XOstate:

    empty = ' '

    def __init__(self):
        self.board = [
                    [XOstate.empty, XOstate.empty, XOstate.empty],
                    [XOstate.empty, XOstate.empty, XOstate.empty],
                    [XOstate.empty, XOstate.empty, XOstate.empty]
                ]
        self.played_moves = 0
        self.current_player = 'x'

    def end(self):
        if self.played_moves == 9:
            return True
        elif self.winner() == 'x' or self.winner() == 'o':
            return True
        else:
            return False

    def play(self, x, y):
        self.board[x][y] = self.current_player
        self.current_player = 'x' if self.current_player == 'o' else 'o'
        self.played_moves += 1

    def draw(self):
        print(" | ".join(self.board[0]))
        print(" | ".join(self.board[1]))
        print(" | ".join(self.board[2]))

    def winner(self):
        for i in range(3):
            if self.board[i][0] != XOstate.empty and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
        for j in range(3):
            if self.board[0][j] != XOstate.empty and self.board[0][j] == self.board[1][j] == self.board[2][j]:
                return self.board[0][j]
        
        if self.board[0][0] != XOstate.empty and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2] != XOstate.empty and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]

    def eval(self):
        w = self.winner()
        if w == 'x':
            return 1
        elif w == 'o':
            return -1
        else:
            return 0

    def get_next_states(self):
        res = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == XOstate.empty:
                    next_state = copy.deepcopy(self)
                    next_state.play(i, j)
                    res.append(next_state)

        return res

def min_value_move(current_state):
    
    if current_state.end():
        return current_state, current_state.eval()

    best_next_state = None
    best_posible_state_eval = float("inf")
    for next_posible_state in current_state.get_next_states():
        _, next_posible_state_eval = max_value_move(next_posible_state)
        if next_posible_state_eval < best_posible_state_eval:
            best_posible_state_eval = next_posible_state_eval
            best_next_state = next_posible_state

    return best_next_state, best_posible_state_eval

def max_value_move(current_state):

    if current_state.end():
        return current_state, current_state.eval()

    best_next_state = None
    best_postible_state_eval = float("-inf")
    for next_posible_state in current_state.get_next_states():
        _, next_posible_state_eval = min_value_move(next_posible_state)
        if next_posible_state_eval > best_postible_state_eval:
            best_postible_state_eval = next_posible_state_eval
            best_next_state = next_posible_state

    return best_next_state, best_postible_state_eval

def main():

    game = XOstate()    

    while not game.end():

        if game.current_player == 'x':
            move_x = int(input())
            move_y = int(input())

            game.play(move_x, move_y)
            game.draw()

        elif game.current_player == 'o':
            game, _ = min_value_move(game)
            game.draw()

    if game.winner() == 'x':
        print("Player X wins")
        exit()
    elif game.winner() == 'o':
        print("Player O wins")
        exit()
    else:
        print("Tie")
        exit()

if __name__ == "__main__":
    main()
