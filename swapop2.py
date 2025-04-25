#swap op2
def swapop():
    a=int(input("enter A value:"))
    b=int(input("enter B value:"))
    a1=(a^b)
    b1=(a^b)
    print("swap({},{})=({},{})".format(a,b,a1,b1))
swapop()
