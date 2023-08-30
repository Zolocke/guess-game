import random

def guess_the_number():
    random_number = random.randint(1, 100)
    num_guesses = 0
    
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            num_guesses += 1
            
            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {random_number} in {num_guesses} guesses.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
