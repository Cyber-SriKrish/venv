#ele op
u=int(input("Enter Unit's You Have Used:"))
bill=500
def hd():
    if((u>=0) and (u<=100)):
        global bill
        print("ELECTRICITY BILL = {}/-RS".format(bill))
def ofy():
    if((u>=101) and (u<=150)):
        global bill
        print("ELECTRICITY BILL = {}/-RS".format(bill+(u-100)*7))
def ofo():
    if((u>=151) and (u<=200)):
        global bill
        print("ELECTRICITY BILL = {}/-RS".format(bill+350+(u-150)*10))
def two():
    if(u>200):
        global bill
        print("ELECTRICITY BILL = {}/-RS".format(bill+850+(u-200)*12))
    
