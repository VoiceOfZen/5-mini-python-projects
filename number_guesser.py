import random

top_of_range = input("Type top number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Type sth larger than zero ")
        quit()
else:
    print('Type an int number ')
    quit()

random_number = random.randint(0, top_of_range)

guesses = 0
hints = 0

while True:
    guesses += 1
    user_guess = input(" Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    elif user_guess == "hint":
        hints += 1
        print(f"Ur rand num was: {random_number}")
    else:
        print('Type a number ')
        continue
    
    if user_guess == random_number:
        print(f"U got it in {guesses} guesses, {hints} hints ")
        break
    elif user_guess < random_number:
        print("higher")
    elif user_guess > random_number:
        print("lower")
    