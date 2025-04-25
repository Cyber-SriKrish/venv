#AF3

def aop(a,b,op):
    if(op=='+'):
        print("SUM({},{})-{}".fotmat(a,b,a+b))
    elif(op=='-'):
        print("sub({},{})={}".format(a,b,a-b))
    elif(op=='*'):
        print("mul({},{})={}".format(a,b,a*b))
    elif(op=='/'):
        print("div({},{})={}".format(a,b,a/b))
    elif(op=='//'):
        print("floor div({},{})={}".format(a,b,a//b))
    elif(op=='%'):
        print("mod div({},{})={}".format(a,b,a%b))
    elif(op=='**'):
        print("expo({},{})={}".format(a,b,a**b))
    else:
        print("INVALID ARTHRMATIC OPERATION")

#by using anonymous functions
sumop=lambda a,b:a+b
subop=lambda a,b:a-b
mulop=lambda a,b:a*b
divop=lambda a,b:a/b
floordivop=lambda a,b:a//b
moddivop=lambda a,b:a%b
expoop=lambda a,b:a**b
#
a=float(input("ENTER FIRST VALUE:"))
b=float(input("ENTER SECOND VALUE:"))
op=str(input("ENTER THE ARTHMETIC OPERATION:"))
aop(a,b,op)
print("------------------------------------")
if(op=='+'):
    print("SUM({},{})-{}".fotmat(a,b,sumop(a,b)))
elif(op=='-'):
    print("sub({},{})={}".format(a,b,subop(a,b)))
elif(op=='*'):
    print("mul({},{})={}".format(a,b,mulop(a,b)))
elif(op=='/'):
    print("div({},{})={}".format(a,b,divop(a,b)))
elif(op=='//'):
    print("floor div({},{})={}".format(a,b,floordivop(a,b)))
elif(op=='%'):
    print("mmod div({},{})={}".format(a,b,moddivop(a,b)))
elif(op=='**'):
    print("expo({},{})={}".format(a,b,expoop(a,b)))
else:
    print("INVALID ARTHRMATIC OPERATION")

