#area of triangle
a=int(input("Enter VAlue Of A:"))
b=int(input("Enter VAlue Of B:"))
c=int(input("Enter VAlue Of C:"))
#calculate s
s=(a+b+c)/2
#calculate area
at=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area Of Triangle:%0.2f"%at)
print("Area Of Triangle:{}".format(round(at,3)))
