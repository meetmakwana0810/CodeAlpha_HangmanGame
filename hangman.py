import random


def play_hangman():
    print("=" * 40)
    print("       WELCOME TO HANGMAN GAME")
    print("=" * 40)

    words = [
        "python",
        "computer",
        "programming",
        "developer",
        "security"
    ]

    secret_word = random.choice(words)

    guessed_letters = []

    max_wrong_guesses = 6
    wrong_guesses = 0

    display_word = ["_"] * len(secret_word)

    print("\nGuess the word one letter at a time!")
    print("You have 6 incorrect guesses.\n")

    while wrong_guesses < max_wrong_guesses:

        print("Word:", " ".join(display_word))

        if guessed_letters:
            print("Guessed letters:", ", ".join(guessed_letters))

        print("Incorrect guesses:", wrong_guesses)
        print()

        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess! ✓\n")

            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    display_word[i] = guess

        else:
            wrong_guesses += 1
            print("Wrong guess! ✗")
            print("Remaining attempts:", max_wrong_guesses - wrong_guesses)
            print()

        if "_" not in display_word:
            print("=" * 40)
            print("🎉 CONGRATULATIONS! YOU WON!")
            print("The word was:", secret_word)
            print("=" * 40)
            break

    else:
        print("=" * 40)
        print("GAME OVER!")
        print("The correct word was:", secret_word)
        print("=" * 40)


play_hangman()