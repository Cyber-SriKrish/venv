a=float(input("enter 1st value:"))
b=float(input("enter 2nd value:"))
c=float(input("enter 3rd value:"))
if (a==b) and (b==c) and (c==a):
    print("all values are equal")
if (a==b)  and (c<=a) and (c<=b):
    print("a and b are biggest")
if (a==c) and (b<=c) and (b<=a):
    print("a and c are biggest")
if (b==c) and (a<=c) and (a<=a):
    print("b and c are biggest")
else:
    big=a
    if(b>=big):
        big=b
        if(c>=big):
            big=c
            print("big({},{},{})={}".format(a,b,c,big))
print("|"*80)

    
       
