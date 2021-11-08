# GAME POD
## About
1. This program holds a suite of games in which the user can interact with the terminal in order to access the games and play.
2. This program contains an Artificial Intelligence system that would play/compete with the user in specific games.
# Hangman
## How to play the game
Hangman is a simple word guessing game. Players try to figure out an unknown word by guessing letters. If too many letters which do not appear in the word are guessed, the player is hanged (and loses).

Setup the game by drawing a gallow and a underline for each letter in the unknown word. As letters in the word are guessed, write them above the cooresponding underline. If a letter not in the word is guess, draw a picture of a person on the gallow–one part for each incorrect letter guess. Most frequently, the person is drawn in 6 parts (for 6 letter guesses) in the order: head, body, left leg, right leg, left arm, right arm.

## instructions
Run the game from the terminal by inserting the command python Hangman.py
# Minesweeper
## How to play the game
A squares "neighbours" are the squares adjacent above, below, left, right, and all 4 diagonals. Squares on the sides of the board or in a corner have fewer neighbors. The board does not wrap around the edges.
If you open a square with 0 neighboring bombs, all its neighbors will automatically open. This can cause a large area to automatically open.
To remove a bomb marker from a square, point at it and right-click again.
The first square you open is never a bomb.
If you mark a bomb incorrectly, you will have to correct the mistake before you can win. Incorrect bomb marking doesn't kill you, but it can lead to mistakes which do.
You don't have to mark all the bombs to win; you just need to open all non-bomb squares.
## instructions
input the row and column in the form (row, column) with a space after the comma, depending on where you want to inveil on the board.

Run the game from the terminal by inserting the command python minesweeper.py
# Tic Tac Toe
## How to play the game
1. The game is played on a grid that's 3 squares by 3 squares.

2. You are X, your friend (or the computer in this case) is O. Players take turns putting their marks in empty squares.

3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.

4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.

5. There are three game modes:
 - Player vs Player
 - Player vs Computer
 - Computer vs Computer

The impossible AI is the Tenet mode in the prompt. 
The game asks the user for their choice of player 1 and player 2.

Run the game from the terminal by inserting the command python game.py

## Extension
We added background sound to play while the program runs. This enhances homeliness on the game