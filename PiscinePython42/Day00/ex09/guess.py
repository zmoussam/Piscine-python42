import random

def guessGame() -> str:
    
    print("This is an interactive guessing game! \n\
You have to enter a number between 1 and 99 to find out the secret number.\n\
Type 'exit' to end the game.\n\
Good luck!\n")

    r = random.randint(1, 10)
    check = True
    count = 0
    while check:
        try:
            guessNumber = input("What's your guess between 1 and 99?\n>> ")
            if (guessNumber == "exit"):
                return "Goodbye!"
            guessNumber = int(guessNumber)
            count += 1
            if guessNumber > r:
                print("Too high!")
            elif guessNumber < r:
                print("Too low!")
            else :
                if r == 42:
                    print("The answer to the ultimate question of life, the universe and everything is 42.")
                if count == 1:
                    return "Congratulations! You got it on your first try!"
                return f'Congratulations, you\'ve got it!\nYou won in {count} attempts!'
        except ValueError:
            print("That's not a number.")

print(guessGame())