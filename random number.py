import random

# print(help(random))

# low = 1
# high = 100
# options = ("rock", "paper", "scissors")
# cards = ["2", "3", "4", "5","6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# # number = random.randint(1, 20)
# # number = random.randint(low, high)
# # number = random.random()
# # option = random.choice(options)
# random.shuffle(cards)
#
#
# # print(number)
# # print(options)
# print(cards)


# number guessing game
import random

lowest_num = 1
highest_num = 10
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python number guessing game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! Try again")
        elif guess > answer:
            print("Too high! Try again")
        else:
            print(f"Correct! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False

    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")


# other code for us to guess
# import random
#
# def guess(x):
#     random_number = random.randint(1, x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f'Guess the number between 1 and {x}: '))
#         if guess < random_number:
#             print('Sorry, guess again. Too low')
#         elif guess > random_number:
#             print('Sorry, guess again. Too high')
#
#     print(f'Yeh, You guessed it correctly')
#
# guess(10)

# code for computer to guess

# def computer_guess(x):
#     low = 1
#     high = x
#     feedback = ''
#
#     while feedback != 'c' and low != high:
#         guess = random.randint(low, high)
#         feedback = input(f'Is {guess} Too high (H), Too low (L), Correct (C)').lower()
#         if feedback == 'h':
#             high = guess - 1
#         elif feedback == 'l':
#             low = guess + 1
#
#     print(f'Yeh, You guessed it correctly')
#
# computer_guess(10)