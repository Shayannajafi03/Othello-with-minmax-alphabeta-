class OthelloAI:
    def __init__(self, game):
        self.game = game
        #assigns values to each square on the board based on its strategic importance
        self.weights = [
            [10, -4, 2, 1, 1, 2, -4, 10],
            [-4, -5, -1, -1, -1, -1, -5, -4],
            [2, -1, 1, 0, 0, 1, -1, 2],
            [1, -1, 0, 0, 0, 0, -1, 1],
            [1, -1, 0, 0, 0, 0, -1, 1],
            [2, -1, 1, 0, 0, 1, -1, 2],
            [-4, -5, -1, -1, -1, -1, -5, -4],
            [10, -4, 2, 1, 1, 2, -4, 10]
        ]

    def minimax(self, depth, maximizing_player, alpha=float('-inf'), beta=float('inf')):
        valid_moves = self.game.valid_moves(self.game.current_player if maximizing_player else -self.game.current_player)
        if depth == 0 or not valid_moves:
            return self.evaluate_board()

        if maximizing_player:
            max_eval = float('-inf')
            for move in valid_moves:
                flipped = self.game.make_move(move[0], move[1], self.game.current_player)
                self.game.switch_player()
                eval = self.minimax(depth - 1, False, alpha, beta)
                self.game.switch_player()
                self.game.undo_move(move[0], move[1], flipped)  # Undo move properly
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:  # Beta cut-off
                    break
            return max_eval
        
        else:
            min_eval = float('inf')
            for move in valid_moves:
                flipped = self.game.make_move(move[0], move[1], -self.game.current_player)
                self.game.switch_player()
                eval = self.minimax(depth - 1, True, alpha, beta)
                self.game.switch_player()
                self.game.undo_move(move[0], move[1], flipped)  # Undo move properly
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:  # Alpha cut-off
                    break
            return min_eval

    def evaluate_board(self):
        score = 0
        player_mobility = len(self.game.valid_moves(1))
        opponent_mobility = len(self.game.valid_moves(-1))
        # TASK 2: implement evaluate_board
        for row in range(8):
            for col in range(8):
                if self.game.board[row][col] == 1:
                    score += self.weights[row][col]
                elif self.game.board[row][col] == -1:
                    score -= self.weights[row][col]

        # Adjust the score based on mobility (favor more mobility)
        # This encourages the AI to prioritize moves that increase its own mobility or limit the opponent's.
        score += player_mobility - opponent_mobility

        return score

    def best_move(self, depth):
        best_eval = float('-inf')
        best_move = None
        for move in self.game.valid_moves(self.game.current_player):
            flipped = self.game.make_move(move[0], move[1], self.game.current_player)
            self.game.switch_player()
            eval = self.minimax(depth - 1, False, float('-inf'), float('inf'))
            self.game.switch_player()
            self.game.undo_move(move[0], move[1], flipped)  # Undo move properly
            if eval > best_eval:
                best_eval = eval
                best_move = move
        return best_move