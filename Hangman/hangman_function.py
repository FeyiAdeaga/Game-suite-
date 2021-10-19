import random


def get_word(word_list):
    length = len(word_list)
    random_word_index = random.randint(1,length)
    random_word = word_list[random_word_index][random_word_index]
    return random_word

def word_set(word):
    letters = set()
    for letter in word:
        letters.add(letter)
    return letters