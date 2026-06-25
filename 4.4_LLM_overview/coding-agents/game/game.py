import random

def number_guessing_game():
    """
    Implements a number guessing game where the user guesses a random 
    number between 1 and 100.
    """
    secret_number = random.randint(1, 100)
    max_tries = 0
    
    print("========================================")
    print("     Welcome to the Number Guessing Game!")
    print("========================================")
    print("I've picked a random number between 1 and 100.")
    print("Try to guess it!")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            max_tries += 1
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
                
            if guess < secret_number:
                print("Too low! 📉")
            elif guess > secret_number:
                print("Too high! 📈")
            else:
                print(f"\n🎉 Correct! The number was {secret_number}!")
                break # Exit the guessing loop
                
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            # Do not increment max_tries for invalid input
            continue
        except EOFError:
            print("\nGame interrupted. Goodbye!")
            break

    # Post-game loop
    while True:
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again == 'yes':
            print("\n" * 2) # Clear screen/add separation
            print("========================================")
            print("     Second Round!")
            print("========================================")
            # Reset tries and start over
            max_tries = 0
            secret_number = random.randint(1, 100)
            continue
        elif play_again == 'no':
            print("\nThanks for playing! Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    number_guessing_game()