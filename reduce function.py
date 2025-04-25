#reduce fun
import functools as r
print("ENTER ELEMENTS SEPERSTED BY SPACE")
lst=[int(val) for val in input().split()]
print("BIGGEST ELEMENT=",r.reduce(lambda x,y:x if x>y else y,lst)) #reduce function belongs to----->functools
print("SMALLEST ELEMENT=",r.reduce(lambda x,y:x if x<y else y,lst))
