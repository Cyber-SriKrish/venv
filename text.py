print("enter text:")
lst=[int(val) for val in input().split()]
lst3=[]
lst2=[]
for val in lst:
    if(len(val)>3):
        val.append(lst3)
    if(len(val)<=2):
        val.append(lst2)
else:
    print("orginal list:".format(lst))
    print("lenght more than three inorginal list:".format(lst3))
    print("lenght less than three inorginal list:".format(lst2))
