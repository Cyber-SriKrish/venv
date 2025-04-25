print("ENTER LIST OF VALUES SEPERATED BY SPACE")
lst=[int(val) for val in input().split()]
print("ALL even VALUES=",list(filter(lambda n: n%2==0,lst)))
print("ALL odd VALUES=",list(filter(lambda n: n%2>0,lst)))
