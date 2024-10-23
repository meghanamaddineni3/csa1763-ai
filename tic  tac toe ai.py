class TicTacToe:
    def __init__(self):
        # Initialize the board and the current player
        self.board = [' ' for _ in range(9)]  # 3x3 board
        self.current_player = 'X'

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

    def make_move(self, position):
        # Make a move on the board
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        return False

    def switch_player(self):
        # Switch the current player
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        while True:
            self.print_board()
            move = int(input(f"Player {self.current_player}, enter your move (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Invalid move. Please enter a number between 1 and 9.")
                continue

            if not self.make_move(move):
                print("This position is already taken. Try again.")
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

            self.switch_player()


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
