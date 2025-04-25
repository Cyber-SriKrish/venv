#anonymous function ex-1
def sumop(a,b):     #NORMAL FUNCTION
    c=a+b
    return c 
addop=lambda a,b:a+b        #anonymous function
#
x1=float(input("ENTER FIRST VALUE:"))
x2=float(input("ENTER SECOND VALUE:"))
res1=sumop(x1,x2)
print("type of sumop=",type(sumop))
print("sum={}".format(res1))
print("|"*50)
print("type of add op=",type(addop))
res2=addop(x1,x2)
print("sum of anonymous fun:{}".format(res2))
