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
          "You have five lives. If you use all five lives"
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


def guess_a_letter(word, blank_word):
    """
    Takes user input, checks it is a single letter that hasn't already
    been guessed, and checks if it is in the word
    """
    guess = input("Guess a letter: ").upper()
    guessed_letters = []

    if guess.isalpha() is False and len(guess) != 1:
        print("Guess must be a single letter. Please guess again")
    elif guess in guessed_letters:
        print("You've already guessed that letter!")
    elif guess in word:
        print("Correct!")
        guessed_letters.append(guess)
        print(guessed_letters)
        # following code adapted from
        # https://www.youtube.com/watch?v=m4nEnsavl6w&ab_channel=Kite
        word_as_list = list(blank_word.split(" "))
        indices = [i for i, letter in enumerate(word) if letter == guess]
        for index in indices:
            word_as_list[index] = guess
        blank_word = "".join(word_as_list)
        print(blank_word)
    else:
        print("Incorrect :(")


def main():
    """
    Runs main game functions
    """
    welcome_message()
    start_game()
    words_to_guess = ["QUAFFLE", "CHAMBER", "PHOENIX", "PENSIEVE", "HORCRUX",
                      "QUIDDITCH", "HUFFLEPUFF", "NIFFLER", "POTIONS", "TROLL"]
    word = new_word(words_to_guess)
    print(f"Word contains {len(word)} letters.")
    print(word)
    blank_word = "_ " * len(word)
    print(blank_word)
    guess_a_letter(word, blank_word)


main()
