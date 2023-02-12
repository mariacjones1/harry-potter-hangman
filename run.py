import random


def welcome_message():
    """
    Prints welcome message and game instructions
    """
    print("Hello and welcome to...\n")
    print("HARRY POTTER HANGMAN!\n")
    print("Instructions:")
    print("Test your knowledge of wizarding words.\n")
    print("For each new round, choose a new letter you think is in the word.")
    print("If you are correct, the letter will be added to the word.")
    print("If you are incorrect, the man will be one step closer ")
    print("to being hanged.\n")
    print("You have five lives. If you use all five lives")
    print("without guessing the word correctly, the man will be hanged and")
    print("you will lose the game.\n")
    print("Now that you know the rules, would you like to play?")


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


def main():
    """
    Runs main game functions
    """
    welcome_message()
    start_game()
    words_to_guess = ["quaffle", "chamber", "phoenix", "pensieve", "horcrux",
                      "quidditch", "hufflepuff", "niffler", "potions", "troll"]
    print(new_word(words_to_guess))


main()
