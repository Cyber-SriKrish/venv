lst=[10,20,30,40,50,78,34,67]
print("elements of list before sort=".format(lst))
lst.sort()
print("elements of list after sort=".format(lst))
for val in lst:
    if(val>=50):
        break
    else:
        print(val)
