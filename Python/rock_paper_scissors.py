from operator import indexOf
import random

print("Rock Paper Scissors")

play=input("Do you want to play? Yes š  or No š¶  ? ")

if play.lower() != "yes":
    print("Let's play some other day! š")
    quit()

print("\nLet's Start š„³\n")

comp=0
user=0
user_choice=""
comp_choice=""

opt=["Rock","Paper","Scissors"]
opt2=["R","P","S"]
print("Enter:\nR: Rock\nP: Paper\nS: Scissors\nQ: Quit")

while True:
    user_choice=input("\nChoose: ").capitalize()

    if user_choice in opt2:
        user_choice=opt[opt2.index(user_choice)]

    if user_choice == "Q":
        print("\nThanks for Playing! š")
        if comp>0 or user>0:
            print(f"\nFinal Score:\nComputer: {comp}  You: {user}\n")
            if(user>comp):
                print("\nš„³ š„³  YOU WON! š„³ š„³\n")
            elif(user<comp):
                print("YOU LOST! š\n")
            else:
                print("š š  DRAW š š\n")
        break

    if user_choice not in opt:
        print("Please choose from the options!")
        continue

    val=random.randint(0,2)
    comp_choice=opt[val]
    print("\nYou Chose:",user_choice)
    print("Computer picked:",comp_choice+"\n")

    if user_choice=="Paper" and comp_choice=="Rock":
        user+=1
        print("Yay! You won š„³\n")
    
    elif user_choice=="Rock" and comp_choice=="Scissors":
        user+=1
        print("Yay! You won š„³\n")

    elif user_choice=="Scissors" and comp_choice=="Paper":
        user+=1
        print("Yay! You won š„³\n")

    elif user_choice==comp_choice:
        #user+=1
        #comp+=1
        print("Draw! š")

    else:
        comp+=1
        print("You Lost! š\nLet's play again!\n")