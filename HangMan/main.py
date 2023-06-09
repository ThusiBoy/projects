stage = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

stage.reverse()

import random

word_list = ["motheo", "lorna", "nkoko", "Tsholo", "thabo", "paballo"]
chosen_word = random.choice(word_list)

lives = 6

display = []
for letter in chosen_word:
    display.append("-")

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter:\n").lower()

    if guess in display:
        print(f"{guess} already guessed, you lose a live")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"{guess} is not in the word, you love a live")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you lose")

    print(f"{' '.join(display)}")

    if "-" not in display:
        end_of_game = True
        print("you win")

    print(stage[lives])

