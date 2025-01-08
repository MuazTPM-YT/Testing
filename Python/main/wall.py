# laptop_on = True
# user = "Muaz"

# if laptop_on:
#     if user == "Muaz":
#         print("Hello Muaz!")
#     else:
#         print("Hello World!")
# else:
#     print("Goodbye World!")


import sys
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QGridLayout,QVBoxLayout, QSizePolicy, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
class TicTacToeWindow(QWidget):
    def _init_(self):
        super()._init_()
        self.b00=QPushButton("X")
        self.b01=QPushButton("O")
        self.b02=QPushButton("X")
        self.b10=QPushButton("O")
        self.b11=QPushButton("X")
        self.b12=QPushButton("O")
        self.b20=QPushButton("X")
        self.b21=QPushButton("O")
        self.b22=QPushButton("X")
        self.label1=QLabel("Welcome to Tic-tac-toe")
        self.label2=QLabel("Player 1's Turn")
        self.initUI()
        self.functionality()
        self.tictactoegrid=[[" " for i  in range(3)] for i in range(3)]
        self.row_count={"X":[0,0,0],"Y":[0,0,0]}
        self.column_count={"X":[0,0,0],"Y":[0,0,0]}
        self.diagonal_count={"X":[0],"Y":[0]}
        self.antidiagonal_count={"X":[0],"Y":[0]}
        self.player="X"
        self.winner=True
        self.i=0
        
    def initUI(self):
        self.setWindowTitle("Razans Tic Tac Toe")
        self.setWindowIcon(QIcon(r"C:\Users\MRaza\Downloads\tic-tac-toe-svgrepo-com.svg"))
        self.setGeometry(675,275,512,512)

        main_layout=QVBoxLayout()

        self.label1.setStyleSheet("font-size: 30px;""font-family: Nebula;")
        self.label2.setStyleSheet("font-size: 20px;""font-family: Nebula;")

        self.label1.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.label2.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)

        hbox=QVBoxLayout()
        hbox.addWidget(self.label1)
        hbox.addWidget(self.label2)

        def button_size_setting(self):
            self.b00.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            self.b00.setFixedSize(150, 150)

            self.b01.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            self.b01.setFixedSize(150, 150)

            self.b02.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            self.b02.setFixedSize(150, 150)

            self.b10.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            self.b10.setFixedSize(150, 150)

            self.b11.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            self.b11.setFixedSize(150, 150)

            self.b12.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            self.b12.setFixedSize(150, 150)
            
            self.b20.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            self.b20.setFixedSize(150, 150)

            self.b21.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            self.b21.setFixedSize(150, 150)

            self.b22.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            self.b22.setFixedSize(150, 150)
        button_size_setting(self)

        grid_layout=QGridLayout()
        def grid_setting(self):
            grid_layout.addWidget(self.b00, 0,0)
            grid_layout.addWidget(self.b01, 0,1)
            grid_layout.addWidget(self.b02, 0,2)
            grid_layout.addWidget(self.b10, 1,0)
            grid_layout.addWidget(self.b11, 1,1)
            grid_layout.addWidget(self.b12, 1,2)
            grid_layout.addWidget(self.b20, 2,0)
            grid_layout.addWidget(self.b21, 2,1)
            grid_layout.addWidget(self.b22, 2,2)

            grid_layout.setHorizontalSpacing(0)
            grid_layout.setVerticalSpacing(10)
        grid_setting(self)

        main_layout.addLayout(hbox)
        main_layout.addLayout(grid_layout)

        main_layout.setSpacing(20)
        self.setLayout(main_layout)

        self.setStyleSheet("""
            QPushButton{
                font-size: 75px;
                font-family: Arial;
                background-color: black;
                color: #39FF14;
                border: 3px solid;
                border-radius: 15px;
            }""")

    def TTT_backend(self,row,column):
        self.i=0
        self.player = "X" if self.i%2==0 else "Y"
        row=int(input(f"{self.player}'s Turn (row)(0/1/2): "))
        column=int(input(f"{self.player}'s Turn: (column)(0/1/2): "))
        self.row_count[self.player][row]+=1
        self.column_count[self.player][column]+=1
        if row==column:
            self.diagonal_count[self.player][0]+=1
        if row+column==2:
            self.antidiagonal_count[self.player][0]+=1
        if self.tictactoegrid[row][column]==' ':
            self.tictactoegrid[row][column]=self.player
        else: 
            print("you cannot make that move")
        if 3 in self.row_count[self.player] or 3 in self.column_count[self.player] or 3 in self.diagonal_count[self.player] or 3 in self.antidiagonal_count[self.player]:
            print(f"{self.player} is the winner")
        self.i+=1

    def functionality(self):
        self.b00.clicked.connect(self.b1_function)
        self.b01.clicked.connect(self.b2_function)
        self.b02.clicked.connect(self.b3_function)
        self.b10.clicked.connect(self.b4_function)
        self.b11.clicked.connect(self.b5_function)
        self.b12.clicked.connect(self.b6_function)
        self.b20.clicked.connect(self.b7_function)
        self.b21.clicked.connect(self.b8_function)
        self.b22.clicked.connect(self.b9_function)

    def b1_function(self):
        print("wot")
    def b2_function(self):
        self.TTT_backend(0,1)
    def b3_function(self):
        self.TTT_backend(0,2)
    def b4_function(self):
        self.TTT_backend(1,0)
    def b5_function(self):
        self.TTT_backend(1,1)
    def b6_function(self):
        self.TTT_backend(1,2)
    def b7_function(self):
        self.TTT_backend(2,0)
    def b8_function(self):
        self.TTT_backend(2,1)
    def b9_function(self):
        self.TTT_backend(2,2)



if __name__=="__main__":
    app=QApplication(sys.argv)
    TicTacToeMain=TicTacToeWindow()
    TicTacToeMain.show()
    sys.exit(app.exec_())