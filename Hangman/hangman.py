import csv
import os
from hangman_function import get_word, lives_visual_dict, music

file = open("wordbank.csv", "r")
csv_reader = csv.reader(file)
word_list = []


def main():

    for row  in csv_reader:
        for word in row:
            word_list.append(row)


    def main_game():
        # word = "friend"
        word = get_word(word_list)
        word = word.strip(" ")
        # word_letters = word_set(word)
        lives = 5
        used_letters = []
        game_list =[letter if letter in used_letters else "_" for letter in word]
        condition = True

        while condition:
            print(game_list)
            user_letter = input().lower()
            os.system('clear')

            if user_letter in word:
                print("correct :D")
                if user_letter in used_letters:
                    print('You have used this letter')
                else:
                    used_letters.append(user_letter)
                    game_list =[letter if letter in used_letters else "_" for letter in word]   
            else:
                print("wrong :C")
                if user_letter not in used_letters:
                    used_letters.append(user_letter)
                    lives -= 1
                else:
                    print('You have used this letter')
            if lives == 0 or "_" not in game_list:
                condition = False
            print(f"You have {lives} lives remaining")
            print(f"You have used these letters:{used_letters}\n")
            print(lives_visual_dict[lives])
            print()


        if lives == 0:
            print("You lose!! :C")
        else:
            print("You win!! :D")
        print(f"Your word was {word}")

        print("Let's play\n")

    main_game()

if __name__ == "__main__":
    music()
    main()