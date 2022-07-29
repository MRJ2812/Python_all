import random

getnum1 = int(input("Enter first  num: "))
getnum2 = int(input("Enter last  num: "))


list1 = []

def game(player_num):
    
    genarate = (random.randint(getnum1,getnum2))
    i = 0
    while True:
    
        get_guess = int(input("Enter your guess:: "))
        
        if get_guess == genarate:
            
            i += 1
            print("\t\t\t Correct guess !!\n")
            print(f"Player {player_num} Total trial = {i} ")
            break

        if get_guess > genarate:
            i += 1
            print("Please enter a smalller number")
            
        if get_guess < genarate:
            i += 1
            print("Please enter a larger number")
    
    
    list1.append(i)
    
    
    
for i in range(2):
    print(f"\nPlayer {i+1}\n")
    game(i+1)

if list1[0] > list1[1]:
    print("Player2 win")
elif list1[0] > list1[1]: 
    print("Player1 win")
    
else:
    print("Match draw... Go home")
