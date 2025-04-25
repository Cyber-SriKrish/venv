def gcd(x,y):
    while x!=y:
        if x>y:
            x=x-y
        else:
            y=y-x

    return x
a=[]
N=int(input("Enter The Numbers:"))
print("Enter the elements:")
for i in range(0,N):
    a.append(int(input()))
g=a[0]
for i in range(1,N):
    g=gcd(g,a[i])
print(g)
