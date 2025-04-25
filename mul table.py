n=int(input("enter a number:"))
print("="*50)
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("="*50)
    print("mul table od{}".format(n))
    i=1
    while(i<=10):
        print("\t{}*{}={}".format(n,i,n*i))
        i=i+1
print("="*50)
