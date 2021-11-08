import random
import pygame

def music():
    pygame.init()
    pygame.mixer.music.load("POL-autumn-leaves-short.wav")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1, 0.0)
    # soundObj = pygame.mixer.Sound("POL-autumn-leaves-short.wav")
    # soundObj.play()


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

lives_visual_dict = {
        0: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / \
               |
           """,
        1: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / 
               |
            """,
        2: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |
            """,
        3: """
                ___________
               | /        | 
               |/        ( )
               |          
               |          
               |
            """,
        4: """
                ___________
               | /        | 
               |/        
               |          
               |          
               |
            """,
        5: """
                ___________
               | /        
               |/        
               |          
               |          
               |
            """,
        6: """
               |
               |
               |
               |
               |
            """,
        7: "",
    }