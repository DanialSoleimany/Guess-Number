import random

start = int(input("Start at:\n"))
stop = int(input("Stop at:\n"))

random_number = random.randint(start, stop)

while True:

    guess_number = int(input(f"Guess a number between {start} to {stop}:\n"))

    if (start > guess_number) or (guess_number > stop):
        print("Out of range!") 
    elif random_number > guess_number:
        print(f"Number is greater than {guess_number}")
    elif random_number < guess_number:
        print(f"Number is smaller than {guess_number}")
    else:
        print("You Won!")
        break