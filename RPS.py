import random
import sys
from enum import Enum

def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2 
        SCISSOR = 3

    playerchoice = input ("\nEnter... \n1 for rock \n2 for paper \n3 for scissor: \n\n")
    if playerchoice not in ["1","2","3"]:
        print("Nhap lai keo,bua,bao: ")
        return play_rps()
    
    player = int(playerchoice)

    computerchoice = random.choice("123")
    computer = int(computerchoice)
    print("\n Your choice: " + str(RPS(player)).replace("RPS.", ""))
    print("\n Your Computer: " + str(RPS(player)).replace("RPS.", ""))
    
    if player == 1 and computer == 3:
        print("\n You win🎈")
    elif player == 2 and computer == 1:
        print("\n You win🎈")
    elif player == 3 and computer == 2:
        print("\n You win🎈")
    elif player == computer :
        print("\n TIE GAME🤣")
    else:
        print("\n YOU ARE A CHICKEN!🔪")

    print("\n PLayer again?")

    while True:
        again = input("\n Y for yes \n Q for quit \n\n")

        if again.lower() not in ["y","q"]:
            print("\nNhap lai")
            continue
        else:
            break
    if (again.lower() == 'y'):
        return play_rps()
    else:
        print("\nEnd game🙋‍♀️🙋‍♀️🙋‍♀️")
        print("Thank you or playing!\n")
        sys.exit("Bye!!!!!!!!!")


play_rps()

