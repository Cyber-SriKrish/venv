a=float(input("enter 1st value:"))
b=float(input("enter 2nd value:"))
c=float(input("enter 3rd value:"))
if((a>b) and (a>c)):
    print(" {} is the biggest".format(a))
if((b>a) and (b>c)):
    print(" {} is the biggest".format(b))
if((c>a) and (c>b)):
    print(" {} is the biggest".format(c))
if (a==b) and (b==c) and (c==a):
    print("all values are equal")
if (a==b)  and (c<=a) and (c<=b):
    print("a and b are biggest")
if (a==c) and (b<=c) and (b<=a):
    print("a and c are biggest")
if (b==c) and (a<=c) and (a<=a):
    print("b and c are biggest")
    
    
       
