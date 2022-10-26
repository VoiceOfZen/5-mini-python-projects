name = input("type your name: ")
print(f"Welcome, \"{name}\" to this adventure!")

answer = input("""U r on a dirt road, it has come to an end and u can go left or right. 
Which way would u like to go? """).lower()

def death():
    print("not a valid option. U've successfully died!")
    quit()

def bad_ending():
    print("Bad Ending")
    quit()

if answer == "left":
    answer = input("""You came to a river, you can walk around it or swim across. 
Type walk to walk around and swim to swim across""").lower()
    if answer == "swim":
        answer = input("""You swam across and magically didn't drown. Congrats! 
Seems like there is a road to the woods, but u can go to the left or right still. 
If u want to go to the woods - type woods, to the left - left, to the right - right :) """).lower()
    elif answer == "walk":
        print()
    else:
        # print("1")
        death()

elif answer == "right":    
    answer = input("You came to a bridge, it looks wobbly. Would u like to cross it or head back? \n (cross/back) \n").lower()
    if answer == "back":
        print("You tried to go back but lost!")
        bad_ending()
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Talk to them? (Y/N) \n ").lower()
        if answer == "y":
            print("?")
        elif answer == "n":
            print("?")
    else:
        # print("3")
        death()

else:
    # print("0")
    death()
print("end")