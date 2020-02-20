"""Built-in Data Types

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview"""


"""Getting the type of the Data"""

a=10
print(type(a)) #intrger

b="hello world"
print(type(b)) #string

c='a'
print(type(c))#string

d=["hi","hello","welcome"]
print(type(d))#list

e=10.0
print(type(e))#float

f=10j
print(type(f))#complex

g=b"Hello world"
print(type(g))#bytes

h=("hi","hello","welcome")
print(type(h))#tuple

i={"name" : "gokul","age" : "20"}
print(type(i))#Dictnaory

j={"hi","hello","welcome"}
print(type(j))#sets

k=True
print(type(k))#boolean

l=bytearray(10)#bytearray
print(type(l))

m=memoryview(bytes(10))
print(type(m))#memoryview

n=range(5)#range
print(type(n))

o=frozenset({"hi","hello"})
print(type(o))

p