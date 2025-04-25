#ams
n=int(input("Enter A Number:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    s=0
    tn=n
    while(n>0):
        d=n%10
        s=s+d**3
        n=n//10
    else:
        if(s==tn):
            print("{} is Amstrong Number:".format(tn))
        else:
            print("{} is not a Amstrong Number:".format(tn))
