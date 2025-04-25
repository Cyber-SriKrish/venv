print("enter number of positive and negative elements seperated by space")
lst=[float(x) for x in input().split()]
print("orginal elements={}".format(lst))
print("\n possitive elements-")
for v in lst:
    if(v<0):
        continue
    print(v,end=" ")
print("-----------\nnegative elements-")
for v in lst:
    if(v>0):
        continue
    else:
        print(v,end=" ")
        
