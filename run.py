import random


def welcome_message():
    """
    Prints welcome message and game instructions
    """
    print("Hello and welcome to...\n"
          "HARRY POTTER HANGMAN!\n"
          "Instructions:"
          "Test your knowledge of wizarding words.\n"
          "For each new round, choose a new letter you think is in the word.\n"
          "If you are correct, the letter will be added to the word.\n"
          "If you are incorrect, the man will be one step closer "
          "to being hanged.\n"
          "You have 7 lives. If you use all 7 lives"
          "without guessing the word correctly, the man will be hanged and"
          "you will lose the game.\n"
          "Now that you know the rules, would you like to play?")


def start_game():
    """
    Ask if user wants to initiate the game and validate answer.
    If user inputs 'Y', continue with code to run game. If user
    imputs 'N', exit code. If user inputs anything else, ask them to
    input either 'Y' or 'N'.
    """
    while True:
        user_start = input("Y/N\n").upper()

        if user_start == "Y":
            break
        elif user_start == "N":
            print("Maybe next time!")
            exit()
        else:
            print(f"Invalid input: {user_start}. Please type 'Y' or 'N'")

    return user_start


def new_word(words):
    """
    Generates the word to guess for the round
    from a given list of words
    """
    word = random.choice(words)

    return word


def play_game(word, blank_word):
    """
    Takes user input, checks it is a single letter that hasn't already
    been guessed, and checks if it is in the word
    """
    guessed_letters = []
    lives = 7

    while lives > 0:
        guess = input("Guess a letter: ").upper()

        if guess.isalpha() is False and len(guess) != 1:
            print("Guess must be a single letter. Please guess again")
        elif guess in guessed_letters:
            print("You've already guessed that letter!")
        elif guess in word:
            print("Correct!\n")
            guessed_letters.append(guess)
            # following code adapted from
            # https://www.youtube.com/watch?v=m4nEnsavl6w&ab_channel=Kite
            word_as_list = list(blank_word)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
            blank_word = "".join(word_as_list)
            if "_" not in blank_word:
                print("Word guessed correctly! You win!")
                print("Would you like to play again?")
                break
        else:
            print("Incorrect :(\n")
            lives -= 1
            guessed_letters.append(guess)
            if lives == 0:
                print("Hangman! Would you like to play again?")
                break

        print(f"{blank_word}\n")
        print(show_hangman(lives))
        print(f"Guessed letters: {guessed_letters}")
        print(f"Remaining lives: {lives}\n")


def show_hangman(lives):
    """
    Shows current hangman state based on remaining lives,
    i.e., 7 remaining lives shows:
    -------
    |      |
    |
    |
    |
    |
    -
    whereas 0 remaining lives shows:
    -------
    |      |
    |      O
    |    \\|/
    |      |
    |     / \\
    -
    """
    if lives == 0:
        hanged_man = """
    -------
    |      |
    |      O
    |     \\|/
    |      |
    |     / \\
    -"""
    elif lives == 1:
        hanged_man = """
    -------
    |      |
    |      O
    |    \\|/
    |      |
    |     /
    -"""
    elif lives == 2:
        hanged_man = """
    -------
    |      |
    |      O
    |     \\|/
    |      |
    |
    -"""
    elif lives == 3:
        hanged_man = """
    -------
    |      |
    |      O
    |     \\|/
    |
    |
    -"""
    elif lives == 4:
        hanged_man = """
    -------
    |      |
    |      O
    |     \\|
    |
    |
    -"""
    elif lives == 5:
        hanged_man = """
    -------
    |      |
    |      O
    |      |
    |
    |
    -"""
    elif lives == 6:
        hanged_man = """
    -------
    |      |
    |      O
    |
    |
    |
    -"""
    elif lives == 7:
        hanged_man = """
    -------
    |      |
    |
    |
    |
    |
    -"""

    return hanged_man


def main():
    """
    Runs main game functions
    """
    welcome_message()
    while True:
        start_game()
        words_to_guess = ["QUAFFLE", "CHAMBER", "PHOENIX", "PENSIEVE",
                          "HORCRUX", "QUIDDITCH", "HUFFLEPUFF", "NIFFLER",
                          "POTIONS", "TROLL"]
        word = new_word(words_to_guess)
        print(f"Word contains {len(word)} letters.")
        print(word)
        blank_word = "_" * len(word)
        print(blank_word)
        play_game(word, blank_word)


main()
