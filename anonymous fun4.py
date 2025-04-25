small=lambda a,b: a if a<b else b  #tenary operator(?)
big=lambda a,b: a if a>b else b
#
a=float(input("ENTER A VALUE:"))
b=float(input("ENTER B VALUE:"))
print("------------------------------------")
if(a==b):
    print("both values are equal")
else:
    print("big({},{})={}".format(a,b,big(a,b)))
    print("small({},{})={}".format(a,b,small(a,b)))

