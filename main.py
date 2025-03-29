import random

def guess(x):
    play_again = 'y'
    while play_again == 'y':
        random_number = random.randint(1, x)
        guess = 0
        while guess != random_number:
            guess = int(input(f'Guess a number between 1 and {x}: '))
            if guess < random_number:
                print('Sorry, guess again. Too low.')
            elif guess > random_number:
                print('Sorry, guess again. Too high.')

        print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'n':
            print("Thanks for playing! Goodbye!")
            break  # Correct placement of the break

def computer_guess(x):
    play_again = 'y'  # Variable to control replay
    while play_again == 'y':  # Loop to allow replaying the game
        low = 1
        high = x
        feedback = ''
        while feedback != 'c':
            if low != high:
                guess = random.randint(low, high)
            else:
                guess = low  # could also be high b/c low = high
            feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
            if feedback == 'h':
                high = guess - 1
            elif feedback == 'l':
                low = guess + 1

        print(f'Yay! The computer guessed your number, {guess}, correctly!')
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'n':
            print("Thanks for playing! Goodbye!")
            break  # Correct placement of the break

guess(40)
