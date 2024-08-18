class OthelloAI:
    def __init__(self, game):
        self.game = game

    def minimax(self, depth, maximizing_player):
        valid_moves = self.game.valid_moves(self.game.current_player if maximizing_player else -self.game.current_player)
        if depth == 0 or not valid_moves:
            return self.evaluate_board()

        # TASK 3: implement minimax algorithm
        if maximizing_player:
            pass 
        else:
            pass
    def evaluate_board(self):
        score = 0
        # TASK 2: implement evaluate_board
        return score

    def best_move(self, depth):
        best_eval = float('-inf')
        best_move = None
        for move in self.game.valid_moves(self.game.current_player):
            self.game.make_move(move[0], move[1], self.game.current_player)
            self.game.switch_player()
            eval = self.minimax(depth - 1, False)
            self.game.switch_player()
            self.game.board[move[0]][move[1]] = 0  # Undo move
            if eval > best_eval:
                best_eval = eval
                best_move = move
        return best_move
