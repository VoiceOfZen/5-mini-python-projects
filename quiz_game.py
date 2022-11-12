print("\n welcome to my quiz")

playing = input("\n Do u wanna play? ").lower()

if playing == "y" or playing == "yes" or playing == "":
    print('\n Okay lets play ')
else:
    print('no is no')
    quit()

score = 0
def score_printer():
    print('\n Your score: ' + str(score))

answer = input("\n What color is Red? \nA. Red \nB. Else \n ").lower()
if answer == "a" or answer == "red":
    print("\n correct")
    score += 1
else:
    print("\n oops, wrong!")

score_printer()

empty = input("\n Empty? ").lower()
if empty == "" or empty ==  "ok":
    print("\n correct")
    score += 1
else:
    print("\n oops, wrong!")

score_printer()

print('\n Final score: ' + str(score/2*100) + "%")