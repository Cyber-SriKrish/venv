#swap op1
def swapop(a,b):
    a=(a^b)
    b=(a^b)
    return(a,b)
a=int(input("enter A value:"))
b=int(input("enter B value:"))
res=swapop(a,b)
print("swap({},{})=({})".format(a,b,res))
