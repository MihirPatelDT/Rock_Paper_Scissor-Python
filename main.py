import random

list = ["rock","paper","scissor"]

com = random.choice(list)

def game(player,com):

    if player==com:
        return None
    
    elif com=="rock":
        if player=="paper":
            return True
        elif player=="scissor":
            return False
        
    elif com=="paper":
        if player=="rock":
            return False
        elif player=="scissor":
            return True
        
    elif com=="scissor":
        if player=="paper":
            return False
        elif player=="rock":
            return True
        
while(True):
    
    print("Computer Turn : Select Rock(r) or Paper(p) or Scissor(s)? : ")
    you = input("Your Turn : Select Rock(r) or Paper(p) or Scissor(s)? or Quit(q) : ")

    if you=="r":
        you="rock"
    elif you=="p":
        you="paper"
    elif you=="s":
        you="scissor"
    elif you=="q":
        break

    result = game(you,com)

    print(f"You Choices : {you}")
    print(f"Computer Choices : {com}")

    if result == None:
        print("The game is a tie!")
    elif result:
        print("You Win!")
    else:
        print("You Lose!")
