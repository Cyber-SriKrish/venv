def findbig(a,b):
    if(a>b):
      return a
    else:
        return b
print("--------------OR---------------")
big=lambda a,b: a if a>b else b  #tenary operator(?)
#
a=float(input("ENTER A VALUE:"))
b=float(input("ENTER B VALUE:"))
findbig(a,b)
print("------------------------------------")
if(a==b):
    print("both values are equal")
else:
    print("big({},{})={}".format(a,b,big(a,b)))

