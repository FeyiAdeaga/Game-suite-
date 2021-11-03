import math
from players import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [" " for space in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():

        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):

        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]

        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]

        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
           
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]



def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_nums()

    letter = 'X'

    status = True


    while status:
        if letter == 'O':
            square = o_player.get_move(game)
       
        else:
            square = x_player.get_move(game)
        
        if game.make_move(square, letter):
            if print_game:
                print(letter + f'makes a move to square {square}')
                game.print_board()
                print('')

        if game.current_winner:
            if print_game:
                print(letter + " wins!!")
            return letter

        if letter == "O":
            letter = "X"
        else:
            letter = "O"

    if print_game:
        print("It's a tie!!!")

        

if __name__ == '__main__':
    tictactoe = TicTacToe()
    print("Select player1: \n 1p for Human player \n com for computer \n Tenet for impossible A.I :D")
    player1 = input()
    print("Select player2: \n 2p for Human player \n com for computer \n Tenet for impossible A.I :D")
    player2 = input()

    if player1 == "1p":
        if player2 == "2p":
            x_player = HumanPlayer("X")
            o_player = HumanPlayer("O")
        elif player2 == "com":
            x_player = HumanPlayer("X")
            o_player = RandomComputerPlayer("O")
        elif player2 == "Tenet":
            x_player = HumanPlayer("X")
            o_player = SmartComputerPlayer("O")

    if player1 == "com":
        if player2 == "2p":
            x_player = RandomComputerPlayer("X")
            o_player = HumanPlayer("O")
        elif player2 == "com":
            x_player = RandomComputerPlayer("X")
            o_player = RandomComputerPlayer("O")
        elif player2 == "Tenet":
            x_player = RandomComputerPlayer("X")
            o_player = SmartComputerPlayer("O")

    if player1 == "Tenet":
        if player2 == "2p":
            x_player = SmartComputerPlayer("X")
            o_player = HumanPlayer("O")
        elif player2 == "com":
            x_player = SmartComputerPlayer("X")
            o_player = RandomComputerPlayer("O")
        elif player2 == "Tenet":
            x_player = SmartComputerPlayer("X")
            o_player = SmartComputerPlayer("O")



    play(tictactoe, x_player, o_player, True)