#eledemo
import sys
from billop import hd,ofy,ofo,two
from billmenu import menu
menu()
u=int(input("Enter Unit's You Have Used Again:"))
try:
    if((u>=0) and (u<=100)):
        hun()
    elif((u>=101) and (u<=150)):
        ofy()
    elif((u>=151) and (u<=200)):
        ofo()
    elif((u>200)):
        two()
except ValueError:
    print("enter only numerical values")
    sys.exit()
        
        
