#find all +ve val's
print("ENTER LIST OF VALUES SEPERATED BY SPACE")
lst=[int(val) for val in input().split()]
def possitive(n):
    if n>0:
        return True
    else:
        return False
def negative(n):
    if n<0:
        return True
    else:
        return False

obj=filter(possitive,lst)
print("TYPE OF OBJ=",type(obj))
pslist=list(obj)
print("ALL POSITIVE VALUES=",pslist)
print("-------------------------------")
nelist=list(filter(negative,lst))
print("ALL NEGATIVE VALUES=",nelist)
