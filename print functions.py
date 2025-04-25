Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> type(a)
<class 'int'>
>>> print(a)
10
>>> print(Hello!)
SyntaxError: invalid syntax
>>> print("Hello!")
Hello!
>>> print("SK=",45)
SK= 45
>>> a=10
>>> b=20
>>> c=a+b
>>> print("sum of ",a,"and",b,"=",c)
sum of  10 and 20 = 30
>>> #sum(10,20)=30
>>> print("sum(",a,")",b,"=",c)
sum( 10 ) 20 = 30
>>> >>> print("sum(",a,"(",b,")=",c)
SyntaxError: invalid syntax
>>> print("sum(",a,"(",b,")=",c)
sum( 10 ( 20 )= 30
>>> a=10
>>> b=20
>>> c=30
>>> d=a+b+c
>>> print("sum of",a,",",b,"and",c,"=",d)
sum of 10 , 20 and 30 = 60
>>> print("sum(",a,",",b,",",c,")=",d)
sum( 10 , 20 , 30 )= 60
>>> a=10
>>> b=20
>>> c=a+b
>>> print("val of a =",a)
val of a = 10
>>> print("val of a={}".format(a))
val of a=10
>>> print("val of b={}".format(b))
val of b=20
>>> print("sum ={}".format(c))
sum =30
>>> print("sum of",a,"and",b,"=",c)
sum of 10 and 20 = 30
>>> print("sum of{} and {}= {}".format(a,b,c))
sum of10 and 20= 30
>>> print("sum({},{},={}".format(a,b,c))
sum(10,20,=30
>>> print("sum({},{})={}".format(a,b,c))
sum(10,20)=30
>>> a=100
>>> print(a)
100
>>> print("val of a=%d"%a)
val of a=100
>>> print("val of a=%f"%a)
val of a=100.000000
>>> print("val of a=%.2f"%a)
val of a=100.00
>>> a="Rossum"
>>> print("name=%s",%a)
SyntaxError: invalid syntax
>>> print("name=%s"%a)
name=Rossum
>>> rno=10
>>> name="rossum"
>>> print("my Rollno:%d and my name:%s"%(rno,name))
my Rollno:10 and my name:rossum
>>> a=10
>>> b=20
>>> c=a+b
>>> print("sum of %d and %d=%f"%(a,b,c))
sum of 10 and 20=30.000000
>>> a=12.34
>>> 