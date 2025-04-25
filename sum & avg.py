#sum and average of n numbers:
def findsum(name,*n,crs="PYTHON"):
    print("Person Name:{} and COURSE:{}".format(name,crs))
    s=0
    for val in n:
        print(val)
        s=s+val
    else:
        print("sum={}".format(s))
        print("|"*80)
        print("avg={}".format(s/len(n)))
        print("|"*80)
        print("|"*80)
print("|"*80)
print("|"*80)
              
findsum("sk",10)
findsum("kris",10,20)
findsum("krish",10,23,45,13,12,-34,66)
findsum("KABALI",10,30,64,72,crs="JAVA")
"findsum("KABALI",crs="JAVA",10,30,64,72)" #we should n't use default parameter as eyword argumens 
"findsum()" #ZeroDivisionError: division by zero

    
