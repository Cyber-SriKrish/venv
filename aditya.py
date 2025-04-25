def dupli():
    try:
        while(True):
            a=list(input("enter a string divided by spaces:").split(" "))
            b=int(input("lenght of string:"))
            if(len(a)==b):
                print(set(a))
            else:
                print("Enter perfect lenght of string that is {}".format(len(a)))
    except ValueError:
        print("only numerical values")
dupli()
