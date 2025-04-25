#swap op4
def swapop():
    a=int(input("A value:"))
    b=int(input("B value:"))
    x=(a^b)
    y=(a^b)
    return a,b,x,y
p,q,r,s=swapop()
print("swap({},{})=({},{})".format(p,q,r,s))
    
