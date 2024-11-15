class TicTacToe:
    def __init__(self,p1):
        self.display_board = [
            "-","-","-",
            "-","-","-",
            "-","-","-"
        ]
        self.game_running = True
        self.turns = []
        self.turn = p1

    def displaying_board(self):
        print("---------")
        for x in range(0,7,3):
            print(f"{self.display_board[x]} | {self.display_board[x+1]} | {self.display_board[x+2]}")
        print("---------")

    def winning_conditions(self):
        if self.display_board[0] == self.display_board[1] == self.display_board[2] != "-": return True
        if self.display_board[3] == self.display_board[4] == self.display_board[5] != "-": return True
        if self.display_board[6] == self.display_board[7] == self.display_board[8] != "-": return True
        if self.display_board[0] == self.display_board[3] == self.display_board[6] != "-": return True
        if self.display_board[1] == self.display_board[4] == self.display_board[7] != "-": return True
        if self.display_board[2] == self.display_board[5] == self.display_board[8] != "-": return True
        if self.display_board[0] == self.display_board[4] == self.display_board[8] != "-": return True 
        if self.display_board[2] == self.display_board[4] == self.display_board[6] != "-": return True
        if "-" not in self.display_board: return False

    def system(self):
        while self.game_running:
            self.displaying_board()
            self.users = int(input(f"{self.turn}'s Turn: "))

            if self.users >= 1 and self.users <= 9:
                if self.turn == p1:
                    if self.users in self.turns:
                        print("---------")
                        print(f"{self.turn} can't take that position")

                    else:
                        for x in range(1,10):
                            if self.users == x: self.display_board[self.users-1] = "X"

                        if self.winning_conditions():
                            self.displaying_board()
                            print(f"{self.turn} Won!")
                            self.game_running = False

                        if self.winning_conditions() == False:
                            self.displaying_board()
                            print("It's a Tie!")
                            self.game_running = False

                        self.turns.append(self.users)
                        self.turn = p2

                elif self.turn == p2:
                    if self.users in self.turns:
                        print("---------")
                        print(f"{self.turn} can't take that position")

                    else:
                        for o in range(1,10):
                            if self.users == o: self.display_board[self.users-1] = "O"

                        if self.winning_conditions():
                            self.displaying_board()
                            print(f"{self.turn} Won!")
                            self.game_running = False

                        if self.winning_conditions() == False:
                            self.displaying_board()
                            print("It's a Tie!")
                            self.game_running = False

                        self.turns.append(self.users)
                        self.turn = p1

                else:
                    print("Unknown Player!")
            else:
                print("You must enter a number between 1-9!")

if __name__ == "__main__":
    p1 = input("Player 1 (X): ").title()
    p2 = input("Player 2 (O): ").title()
    ttt = TicTacToe(p1)
    ttt.system()