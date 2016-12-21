import random

print('Welcome User! You are about to play the guessing game enjoy!')

# Generate a random Int number between (x <= n <= y)
randomNumber = random.randint(0, 10)

# User has 3 guesses before losing the game
numberOfGuesses = 0

while numberOfGuesses < 3:

    # Get users input
    userInput = int(input("Give me your best guess: "))

    # Computer tells user whether guess was too high or too low
    if userInput == randomNumber:

        print('Good guess')
        print('You are correct, you won!')
        break

    elif userInput > randomNumber:

        print('Sorry, you guessed too high!')

    elif userInput < randomNumber:

        print('Sorry, you guessed too low!')

    numberOfGuesses += 1


if numberOfGuesses == 3:

    print('You lost!')
