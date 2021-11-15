from replit import audio
from hangman import play_hangman
from tictactoe import play_tictactoe
from minesweeper import play_minesweeper

status = True 

while status:

    # source = audio.play_file('POL-autumn-leaves-short.wav')

    game_choice = input("What game are do you want to play? \n 1 for Hangman \n 2 for TicTacToe\n 3 for minesweeper\n")
    if game_choice.isdigit():
        choice = int(game_choice)

        if choice == 1:
            play_hangman()
        elif choice == 2:
            play_tictactoe()
        else:
            play_minesweeper()

    ask = input("Play again?: \n Y for yes. N for No\n").lower()
    if ask == "n":
        status = False

print("Thanks for Playing!!!!✌✌")