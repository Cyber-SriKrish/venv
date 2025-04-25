Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> d1={10:"apple",20:"mango",30:"kiwi"}
>>> print(d1,type(d1))
{10: 'apple', 20: 'mango', 30: 'kiwi'} <class 'dict'>
>>> id(d1)
140291154778304
>>> d1[2]=15
>>> d1,id(d1)
({10: 'apple', 20: 'mango', 30: 'kiwi', 2: 15}, 140291154778304)
>>> d1[20]="STRAWBERRY"
>>> d1,id(d1)
({10: 'apple', 20: 'STRAWBERRY', 30: 'kiwi', 2: 15}, 140291154778304)
>>> d1={}
>>> d2=dict()
>>> print(d1,type(d1),id(d1))
{} <class 'dict'> 140291154810944
>>> print(d2,type(d2),id(d2))
{} <class 'dict'> 140291150561728
>>> d1[10]="sachin"
>>> d1[20]="sagar"
>>> d1[30]="rohit"
>>> d1[40]="sachin"
>>> print(d1,type(d1),id(d1))
{10: 'sachin', 20: 'sagar', 30: 'rohit', 40: 'sachin'} <class 'dict'> 140291154810944
>>> d2["rossum"=1234
   
SyntaxError: invalid syntax
>>> d2["rossum"]=1234
>>> d2["james"]=5678
>>> d2["ritche"]=9999
>>> d2[1234]="trump"
>>> print(d2,type(d2),id(d2))
{'rossum': 1234, 'james': 5678, 'ritche': 9999, 1234: 'trump'} <class 'dict'> 140291150561728
>>> d1={10: 'apple', 20: 'mango', 30: 'kiwi'}
>>> print(d1,type(d1),id(d1))
{10: 'apple', 20: 'mango', 30: 'kiwi'} <class 'dict'> 140291154612032
>>> d1[40]="guava"
>>> print(d1,id(d1),type(d1))
{10: 'apple', 20: 'mango', 30: 'kiwi', 40: 'guava'} 140291154612032 <class 'dict'>
>>> d1={10: 'apple', 20: 'mango', 30: 'kiwi'}
>>> d1
{10: 'apple', 20: 'mango', 30: 'kiwi'}
>>> d1.clear
<built-in method clear of dict object at 0x7f9814227fc0>
>>> d1.clear()
>>> d1
{}
>>> d1={10: 'apple', 20: 'mango', 30: 'kiwi'}
>>> d1,id(d1)
({10: 'apple', 20: 'mango', 30: 'kiwi'}, 140291151299520)
>>> d2=d1.copy()
>>> d2,id(d2)
({10: 'apple', 20: 'mango', 30: 'kiwi'}, 140291154612032)
>>> d2[20]=["sberry"]
>>> d2
{10: 'apple', 20: ['sberry'], 30: 'kiwi'}
>>> d1
{10: 'apple', 20: 'mango', 30: 'kiwi'}
>>> 
>>> d1=
SyntaxError: invalid syntax
>>> d1
{10: 'apple', 20: 'mango', 30: 'kiwi'}
>>> d2=d1.get(20)
>>> d2
'mango'
>>> d3=d1.get("banana")
>>> d3
>>> d3
>>> print(d3)
None
>>> d1
{10: 'apple', 20: 'mango', 30: 'kiwi'}
>>> id(d1)
140291151299520
>>> d1.pop(30)
'kiwi'
>>> d1,id(d1)
({10: 'apple', 20: 'mango'}, 140291151299520)
>>> d1
{10: 'apple', 20: 'mango'}
>>> v=d1.pop(20)
>>> d1
{10: 'apple'}
>>> v
'mango'
>>> d1.pop(100)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    d1.pop(100)
KeyError: 100
>>> d1={10: 'apple', 20: 'mango', 30: 'kiwi'}
>>> d1.popiteam()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    d1.popiteam()
AttributeError: 'dict' object has no attribute 'popiteam'
>>> d1.popiteam()
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    d1.popiteam()
AttributeError: 'dict' object has no attribute 'popiteam'
>>> d1.popitem()
(30, 'kiwi')
>>> d1.popitem()
(20, 'mango')
>>> d1.popitem()
(10, 'apple')
>>> d1.popitem()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    d1.popitem()
KeyError: 'popitem(): dictionary is empty'
>>> d1
{}
>>> d1={10: 'apple', 20: 'mango', 30: 'kiwi'}
>>> d1.keys()
dict_keys([10, 20, 30])
>>> k=d1.keys()
>>> print(k,type(K))
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    print(k,type(K))
NameError: name 'K' is not defined
>>> print(k,type(k))
dict_keys([10, 20, 30]) <class 'dict_keys'>
>>> for kv in k:
	print(kv)

	
10
20
30
>>> for k in d.keys()
SyntaxError: invalid syntax
>>> for k in d1.keys():

	print(k)

	
10
20
30
>>> d1
{10: 'apple', 20: 'mango', 30: 'kiwi'}
>>> for v in d1.values():
	print(v)

	
apple
mango
kiwi
>>> d1
{10: 'apple', 20: 'mango', 30: 'kiwi'}
>>> for i in d1.items():
	print(i)

	
(10, 'apple')
(20, 'mango')
(30, 'kiwi')
>>>  type(i)
 
SyntaxError: unexpected indent
>>> type(i)
<class 'tuple'>
>>> d1
{10: 'apple', 20: 'mango', 30: 'kiwi'}
>>> i=d1.items()
>>> i,type(i)
(dict_items([(10, 'apple'), (20, 'mango'), (30, 'kiwi')]), <class 'dict_items'>)
>>> v,type(v)
('kiwi', <class 'str'>)
>>> for i1,i2 in d1.items():
	print(i1"---->"i2)
	
SyntaxError: invalid syntax
>>> 
>>> l1=[10,20,30]
>>> l2=["ramu","rahul","rajesh"]
>>> l3=["c","cpp","python"]
>>> for a,b,c in l1,l2,l3:
	print(a,b,c)

	
10 20 30
ramu rahul rajesh
c cpp python
>>> zip(l1,;2,l3)
SyntaxError: invalid syntax
>>> zip(l1,l2,l3)
<zip object at 0x7f98143e45c0>
>>> z=zip(l1,l2,l3)
>>> print(z,type(z))
<zip object at 0x7f98143e4e80> <class 'zip'>
>>> for rno,name,sk in z:
	print(rno,"-->",name,"-->",sk)

	
10 --> ramu --> c
20 --> rahul --> cpp
30 --> rajesh --> python

------------UPDATE---------------------
>>> d1={stno":10,"name":"rajesh"}
>>> d2={"sub1":"python","sub2":"java"}
>>> d1.update(d2)
>>> d1
{'stno': 10, 'name': 'rajesh', 'sub1': 'python', 'sub2': 'java'}
        
