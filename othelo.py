class Othello:
    def __init__(self):
        self.board = [[0] * 8 for _ in range(8)]  # 0: empty, 1: player 1, -1: player 2
        self.board[3][3] = self.board[4][4] = 1
        self.board[3][4] = self.board[4][3] = -1
        self.current_player = 1

    def print_board(self):
        for row in self.board:
            print(' '.join(['.' if x == 0 else 'X' if x == 1 else 'O' for x in row]))
        print()

    def valid_moves(self, player):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        moves = []
        for r in range(8):
            for c in range(8):
                if self.board[r][c] == 0:
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < 8 and 0 <= nc < 8 and self.board[nr][nc] == -player:
                            while 0 <= nr < 8 and 0 <= nc < 8:
                                if self.board[nr][nc] == 0:
                                    break
                                if self.board[nr][nc] == player:
                                    moves.append((r, c))
                                    break
                                nr += dr
                                nc += dc
        return list(set(moves))

    def make_move(self, row, col, player):
        if (row, col) not in self.valid_moves(player):
            raise ValueError("Invalid move")
        
        self.board[row][col] = player
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        flipped = []  # List to store flipped pieces
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            flip_positions = []
            while 0 <= nr < 8 and 0 <= nc < 8:
                if self.board[nr][nc] == 0:
                    break
                if self.board[nr][nc] == player:
                    for fr, fc in flip_positions:
                        self.board[fr][fc] = player
                        flipped.append((fr, fc))  # Track flipped pieces
                    break
                flip_positions.append((nr, nc))
                nr += dr
                nc += dc
        return flipped

    def undo_move(self, row, col, flipped):
        self.board[row][col] = 0  # Undo the move
        for fr, fc in flipped:
            self.board[fr][fc] *= -1  # Flip the pieces back

    def has_valid_move(self, player):
        return len(self.valid_moves(player)) > 0

    def switch_player(self):
        self.current_player *= -1
