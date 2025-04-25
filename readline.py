#readlines:
try:
    fname=input("enter any file name=")
    with open("fname","r")as fp:
        filedata=fp.readlines()
        print("type of vardata=",typr(filedata))
        for line in filedata:
            print(line,end="")
except FileNotFoundError:
    print("Try Again")
