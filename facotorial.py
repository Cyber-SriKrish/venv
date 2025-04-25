n=int(input("enter any integer:"))
print("="*50)
if(n<0):
    print("{}is invalid input".format(n))
else:
    if(n==0):
        print("factorial is 1")
    else:
        print("="*50)
        print("factotials for :{}".format(n))
        print("="*50)
        f=1
        i=1
        while(i<=n):
            f=f*i
            i+1
        else:
            print("="*50)
            print("{} factorials are:{}".format(n,f))
            print("="*50)
    
