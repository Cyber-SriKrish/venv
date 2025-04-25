#prime numbers
n=int(input("Enter A Number:"))
if(n<=1):
    print("{} is invalid input".format(n))
else:
    found=False
    for i in range(2,n):
        if(n%i==0):
            found=True
            break
    if(found==True):
        print("{} is not a prime number".format(n))
    else:
        print("{} is a prime number".format(n))
