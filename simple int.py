#SI acts as module name
def si():
    p=float(input("ENTER PRINCIPLE AMMOUNT:"))
    t=float(input("ENTER TIME:"))
    r=float(input("ENTER RATE OF INTREST:"))
    si=((p*t*r)/100)
    print("principle ammount=",p)
    print("time period=",t)
    print("rate of intrest=",r)
    print("SIMPLE INTREST=",si)
    print("TOTAL AMMOUT TO PAY=",p+si)
#
si()
              
