on=int(input("enter ant number :"))
if(on<0):
    print("{} is invalid input".format(on))
else:
    print("orginal number={}".format(on))
    rn=0
    while(on>0):
        d=on%10
        rn=rn*10+d
        on=on//10
    else:
        print("reversesd number = {}".format(rn))
        if(rn==on):
            print("given number is palindrome")
        else:
            print("given number is not palindrome")
