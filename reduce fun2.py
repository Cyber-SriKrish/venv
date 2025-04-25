#reduce fun
import functools as r
print("ENTER ELEMENTS SEPERSTED BY SPACE")
lst=[int(val) for val in input().split()]
print("SUM OF ELEMENTs=",r.reduce(lambda x,y:x+y,lst))
print("PRODUCT OF ELEMENTs=",r.reduce(lambda x,y:x*y,lst))
