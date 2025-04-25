#whether the no is +ve,-ve,0
n=float(input("enter n value:"))
if(n==0):
    print("{} value is zero".format(n))
else:
    if(n<0):
        print("{} is negative value".format(n))
    else:
        print("{} is possitive value".format(n))
print("|"*80)
