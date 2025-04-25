print("enter number of values seperated by space :")
orglst=[int(val)for val in input().split()]
poslst=[]
neglst=[]
for val in orglst:
    if(val>0):
        poslst.append(val)
    if(val<0):
        neglst.append(val)
    else:
        print("zero values are in valid")
else:
    print("\n orginal list values={}".format(orglst))
    print("\n positive list values={}".format(poslst))
    print("\n negative list values={}".format(neglst))
