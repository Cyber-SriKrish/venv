# to cal compound intrest
p=float(input("enter Principle Ammount ="))
t=float(input("enter Time (in years) ="))
r=float(input("enter Rate Of Intrest ="))
n=float(input("enter the no of times compound intrest per year = "))
r=r/100 #conversion
a=(p)*(1+(r/n))**(n*t)
cp=a-p
print("="*30)
print("="*30)
print("="*30)
print("COMPOUND INTREST = {}".format(cp))
print("="*30)
print("="*30)
print("TOTAL AMMOUNT = {}".format(a))
print("="*30)
print("="*30)
print("="*30)
