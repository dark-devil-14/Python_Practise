"""
sanke  --> 1
water  --> -1
gun.  -->  0
"""

usr_dict = {"s": 1, "w": -1, "g": 0}
reverse = {1: "snake",-1: "water", 0: "gun" }
import random
options = [-1, 0, 1]

def game_setting(system,usr):
    if(system == -1 and usr == 1):
        print("You  Won!! ")
    elif(system == -1 and usr == 0):
        print("You Loose.. ")
    elif(system == 0 and usr == 1):
        print("You Loose.. ")
    elif(system == 0 and usr == -1):
        print("You Won!! ")
    elif(system == 1 and usr == -1):
        print("You Loose.. ")
    elif(system == 1 and usr == 0):
        print("You Won!! ")
    elif( system == usr ):
        print("Ohh that's a tie go ahead and try again... ")
    else:
        print("Something wenth wrong.")
        return True
    
while(1):
    system = random.choice(options)
    #Error Handling 
    try:
        usr_choice = (input("Enter Your Choice: "))
        usr = usr_dict[usr_choice]
        print(f"You chose: {reverse[usr]}")
        print(f"System chose: {reverse[system]}")
        game_setting(system, usr)

    except KeyError:
        print("Invalid input, try again.\n")

