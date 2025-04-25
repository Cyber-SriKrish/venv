print("ENTER LIST OF VALUES SEPERATED BY SPACE")
lst=[int(val) for val in input().split()]
pslist=list(filter(lambda n: n>0,lst))
print("ALL POSITIVE VALUES=",pslist)
print("-------------------------------")
nelist=list(filter(lambda n: n<0,lst))
print("ALL NEGATIVE VALUES=",nelist)

print("-------------------------------")
print("-------------------------------")
print("ENTER LIST OF VALUES SEPERATED BY SPACE")
lst=[int(val) for val in input().split()]
print("ALL POSITIVE VALUES=",list(filter(lambda n: n>0,lst)))
print("ALL -ve VALUES=",list(filter(lambda n: n<0,lst)))
