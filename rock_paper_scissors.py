import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors", "hint"]
#            0        1         2          3


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit:  ").lower()
    
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]

    if user_input == "q":
        break
    elif user_input not in options:
        continue
    elif user_input == 'hint':
        print(computer_pick) 
        while user_input == options:
            user_input = input("Type Rock/Paper/Scissors or Q to quit:  ").lower()

    
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won")
        user_wins += 1
        continue
    elif user_input == "paper" and computer_pick == "rock":
        print("You won")
        user_wins += 1
        continue
    elif user_input == "rock" and computer_pick == "scissors":
        print("You won")
        user_wins += 1
        continue
    else:
        print("U lost!")
        computer_wins += 1
    print("Computer picked", computer_pick + ".")

        # if user_input == "scissors" and computer_pick == "paper":
        #     print("You won")
        #     user_wins += 1
        #     continue
        # elif user_input == "paper" and computer_pick == "rock":
        #     print("You won")
        #     user_wins += 1
        #     continue
        # elif user_input == "rock" and computer_pick == "scissors":
        #     print("You won")
        #     user_wins += 1
        #     continue
        # else:
        #     print("U lost!")
        #     computer_wins += 1
        # print("Computer picked", computer_pick + ".")

    # if user_input == "scissors" and computer_pick == "paper":
    #     print("You won")
    #     user_wins += 1
    #     continue
    # elif user_input == "paper" and computer_pick == "rock":
    #     print("You won")
    #     user_wins += 1
    #     continue
    # elif user_input == "rock" and computer_pick == "scissors":
    #     print("You won")
    #     user_wins += 1
    #     continue
    # else:
    #     print("U lost!")
    #     computer_wins += 1
    # print("Computer picked", computer_pick + ".")
print(f"You won {user_wins} times")   
print(f"Random won {computer_wins} times")   
print('Goodbye!')