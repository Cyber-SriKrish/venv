#bankingop
from atmexp import DepositError,WithDrawError,InSufficientError
bal=25000.00
def deposit():
    damt=float(input("Enter The Ammount To Ammount:"))
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("\n ur Account xxxxxxxx123 credited with INR;{}".format(damt))
        print("Now Ur Current BAl:{}".format(bal))
def withdraw():
    global bal
    wamt=float(input("Enter Withdrawl ammount:"))
    if(wamt<=0):
        raise WithDrawError
    elif((wamt+500)>bal):
        raise InSufficientError
    else:
        if(wamt<bal):
            bal=bal-wamt
            print("Ur Accour xxxxx123 debited with INR:{}".format(wamt))
            print("Now Ur Current BAl:{}".format(bal))
def balenq():
    print("Ur account XXXXX123 Balance is:{}".format(bal))
