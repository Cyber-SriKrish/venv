#atm demo
import sys
from atmmenu import atmmenu
from atmop import deposit,withdraw,balenq
from atmexp import DepositError,WithDrawError,InSufficientError
while(True):
    try:
        atmmenu()
        ch=int(input("enter your choice:"))
        if(ch==1):
            try:
                deposit()
            except ValueError:
                print("enter only numerical values")
            except DepositError:
                print("\n not able to add ammount less than 10RS")
        elif(ch==2):
            try:
                withdraw()
            except ValueError:
                print("enter only numerical values")
            except WithDrawError:
                print("\n enter correct input")
            except InSufficientError:
                print("insuffficient bal")
        elif(ch==3):
            try:
                balenq()
            except ValueError:
                print("enter only numerical values")
        elif(ch==4):
            print("THANKS FOR USING THIS APP")
            sys.exit()
        else:
            print("INVALID INPUT ENTER AGAIN")
    except ValueError:
        print("alpha numerical values invalid")
