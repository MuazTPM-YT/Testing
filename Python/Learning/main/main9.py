class TicTacToe:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.row_counts = {'X': [0, 0, 0], 'O': [0, 0, 0]}
        self.col_counts = {'X': [0, 0, 0], 'O': [0, 0, 0]}
        self.main_diag_counts = {'X': 0, 'O': 0}  
        self.anti_diag_counts = {'X': 0, 'O': 0} 
        self.BLANK = ''
        self.size = 3

    def make_move(self, player, row, col):
        if self.board[row][col] != self.BLANK:
            raise ValueError("You can't play there")
        self.board[row][col] = player

        self.row_counts[player][row] += 1
        self.col_counts[player][col] += 1
        if row == col:
            self.main_diag_counts[player] += 1
        if row + col == self.size - 1:
            self.anti_diag_counts[player] += 1

    def check_for_win(self, player):
        return (
            self.size in self.row_counts[player] or
            self.size in self.col_counts[player] or
            self.main_diag_counts[player] == self.size or
            self.anti_diag_counts[player] == self.size
        )

    def is_draw(self):
        return all(
            self.board[row][col] != self.BLANK
            for row in range(self.size)
            for col in range(self.size)
        )

game = TicTacToe()

game.make_move('X', 0, 0)  
game.make_move('O', 1, 1)  
game.make_move('X', 0, 1) 
game.make_move('O', 2, 2) 
game.make_move('X', 0, 2)  

if game.check_for_win('X'):
    print("Player X wins!")
elif game.check_for_win('O'):
    print("Player O wins!")
elif game.is_draw():
    print("The game is a draw!")
else:
    print("No winner yet.")

