n=int(input("enter any integer:"))
print("="*50)
i=1
while(i<=10):
    i=i+1
    f=n%i
    if(n%i==0):
        print("Factors of {} is {}".format(n,i))
