#opening the file in R operation and Read mode.
try:
    fp=open("sk.py","r")
    print("Type Of file pointer=",type(fp))
except FileNotFoundError:
    print("sk")
else:
    print("\n File Opened in Read Mode sucessfully")
    print("Name of Mode=",fp.mode)
    print("Can We Write=",fp.writable())
    print("Can We read=",fp.readable())
    print("is File closed=",fp.closed)
finally:
    print("FInally   ")
    if(fp!=None):
        print("File cLosed")
        fp.close()
        print("is File closed=",fp.closed)
