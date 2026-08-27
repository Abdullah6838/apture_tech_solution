import random

def number_guessing_game():
    print("=== WELCOME TO NUMBER GUESSING GAME ===")
    print("I have chosen a number between 0 and 9. Can you guess it?")

    guess_number = int(''.join(random.sample("1234567890", k = 1)))
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (0-9): "))
            attempts += 1

            if guess > 9:
                print("[!] Please keep your guess between 1 and 100.")
            elif guess < guess_number:
                print("Too low! Try a higher number.")
            elif guess_number > guess_number:
                print("Too high! Try a higher number.")
            else:
                print(f"\n🎉 Congratulations! You guessed the number in {attempts} attempts!")
                break

        except ValueError:
            print("[!] Invalid input! Please enter a valid whole number.")

    play_again = input("Would you like to play again? (yes/no): ")
    if play_again in ["y", "yes"]:
        print("\n" + "="*40 + "\n")
        number_guessing_game()
    else:
        print("Thanks for playing! Goodbye.")

number_guessing_game()