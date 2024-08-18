from othelo import Othello
from bot import OthelloAI

def play_othello():
    game = Othello()
    ai = OthelloAI(game)

    while True:
        game.print_board()
        if game.has_valid_move(game.current_player):
            if game.current_player == 1:  # Human player
                print("moves: ", game.valid_moves(game.current_player))
               
                row, col = map(int, input("Enter your move (row col): ").split())
                if (row, col) in game.valid_moves(game.current_player):
                    game.make_move(row, col, game.current_player)
                else:
                    print("Invalid move. Try again.")
                    continue
            else:  # AI player
                print("AI is making a move...")
                move = ai.best_move(depth = 3)   #TASK 1: find the best depth
                if move:
                    game.make_move(move[0], move[1], game.current_player)
                    print(f"AI played: {move}")
        else:
            print(f"Player {game.current_player} has no valid moves.")
        
        game.switch_player()

        if not game.has_valid_move(game.current_player):
            print("Game over!")
            break

    game.print_board()
    score = sum(sum(row) for row in game.board)
    if score > 0:
        print("Player 1 (X) wins!")
    elif score < 0:
        print("Player 2 (O) wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_othello()
