#find all +ve val's
possitive=lambda n: n>0
negative=lambda n: n<0
#
print("ENTER LIST OF VALUES SEPERATED BY SPACE")
lst=[int(val) for val in input().split()]
obj=filter(possitive,lst)
print("TYPE OF OBJ=",type(obj))
pslist=list(obj)
print("ALL POSITIVE VALUES=",pslist)
print("-------------------------------")
nelist=list(filter(negative,lst))
print("ALL NEGATIVE VALUES=",nelist)
