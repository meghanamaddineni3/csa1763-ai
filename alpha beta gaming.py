import math

class TicTacToe:
    def __init__(self):
        # Initialize the board
        self.board = [' ' for _ in range(9)]  # 3x3 board
        self.current_player = 'X'  # Computer is 'X'

    def print_board(self):
        # Print the current state of the board
        print("Current board:")
        for i in range(3):
            print(f"| {' | '.join(self.board[i*3:(i+1)*3])} |")
            if i < 2:
                print("---------------")

    def check_winner(self):
        # Check all winning combinations
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
            (0, 4, 8), (2, 4, 6)               # Diagonal
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]
        return None

    def is_draw(self):
        # Check if the board is full (draw)
        return ' ' not in self.board

    def make_move(self, position, player):
        # Make a move on the board
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        return False

    def alpha_beta(self, depth, alpha, beta, is_maximizing):
        winner = self.check_winner()
        if winner == 'X':
            return 10 - depth  # Computer's win
        elif winner == 'O':
            return depth - 10  # Opponent's win
        elif self.is_draw():
            return 0  # Draw

        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'X'  # Computer's move
                    score = self.alpha_beta(depth + 1, alpha, beta, False)
                    self.board[i] = ' '  # Undo move
                    best_score = max(best_score, score)
                    alpha = max(alpha, score)
                    if beta <= alpha:  # Beta cut-off
                        break
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'O'  # Opponent's move
                    score = self.alpha_beta(depth + 1, alpha, beta, True)
                    self.board[i] = ' '  # Undo move
                    best_score = min(best_score, score)
                    beta = min(beta, score)
                    if beta <= alpha:  # Alpha cut-off
                        break
            return best_score

    def find_best_move(self):
        best_score = -math.inf
        best_move = None
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'X'  # Computer's move
                score = self.alpha_beta(0, -math.inf, math.inf, False)
                self.board[i] = ' '  # Undo move
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move

    def play(self):
        while True:
            self.print_board()
            if self.current_player == 'X':  # Computer's turn
                move = self.find_best_move()
                self.make_move(move, 'X')
                print(f"Computer chose position {move + 1}")
            else:  # Player's turn
                move = int(input("Your move (1-9): ")) - 1
                if move < 0 or move > 8 or not self.make_move(move, 'O'):
                    print("Invalid move. Try again.")
                    continue

            winner = self.check_winner()
            if winner:
                self.print_board()
                print(f"Player {winner} wins!")
                break
            
            if self.is_draw():
                self.print_board()
                print("It's a draw!")
                break

            # Switch player
            self.current_player = 'O' if self.current_player == 'X' else 'X'


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
