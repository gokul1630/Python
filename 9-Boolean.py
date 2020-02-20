
"""Booleans

Booleans are only true or false & 0 or 1"""

print(10<9) #10 is lesser than 9
print(2>1) # 1 is greater than 2 
print(1==1) # 1 is equal to 

"""Evaluate Values and Variables
The bool() function allows you to evaluate any value, and give you True or False in return"
here we can print tuples,dicts,sets,lists in bool empty values are always returned to false

Most Values are True
Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones."""


print("\n")
a="hi"
b = 10
#All conditions are returns true
print(bool(a))
print(bool(b))
print(bool("hello world"))
print(bool(["asus", "redmi", "apple"]))

"""Some Values are False
In fact, there are not many values that evaluates to False, except empty values, such as (), [], {}, "", the number 0, 
and the value None. And of course the value False evaluates to False.

All conditions with empty strings & values are returned as false"""
print("\n")
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


"""
Functions can Return a Boolean
Python also has many built-in functions that returns a boolean value, like the isinstance() function, 
which can be used to determine if an object is of a certain data type:
"""

a=100
print(isinstance(a, int))