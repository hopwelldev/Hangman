import random
import hangman_words
import hangman_art

# VARS
lives = 6
game_end = False
display = []

# RANDOMIZATION
rand_numb = random.randint(0, len(hangman_words.word_list) - 1)
chosen_word = hangman_words.word_list[rand_numb]
print(chosen_word)

# SETTING UP DISPLAY
for _ in range(len(chosen_word)):
    display.append("_")
print(display)

# REVEALING LETTERS
print(hangman_art.logo)
while not game_end:
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter
    if guess not in chosen_word:
        print(hangman_art.stages[lives])
        lives -= 1

    print(display)

    # GAME CHECKING CONDITIONS
    if "_" not in display:
        game_end = True
        print("You win!")
    if lives == -1:
        game_end = True
        print("You lose!")