#argu passing parameter(possitional,default)
def dispstudinfo(stno,sname,smarks,scour,ins="NIT",cnt="INDIA"):
    print("="*50)
    print("------------Student Information------------")
    print("\tID\tNAME\tMARKS\tCOURSE\tINSTITUTE\tCOUNTRY")
    print("\t{}\t{}\t{}\t{}\t{}\t{}".format(stno,sname,smarks,scour,ins,cnt))
    print("="*50)
    print("="*50)
#
a=int(input("Enter Student Number:"))
b=str(input("Enter Student Name:"))
c=float(input("Enter Student marks:"))
d=str(input("Enter Student course:"))
dispstudinfo(a,b,c,d) #function call
