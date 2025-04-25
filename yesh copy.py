#import math
#def solve(N,A,P):
    #G=[]
    #for i in range(0,N):
        G.append(int(mth.gcd(*A)))
        A[P[i]-1]=0
    return(sum(G))

N=int(input())
A=[]
for _ in range(N):
    A.append(int(input()))
P=[]
for _ in range(N):
    P.append(int(input()))
result=solve(N,A,P)
print(result)


        
