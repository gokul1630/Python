"""List is a collection which is ordered and changeable. Allows duplicate members."""


a=["this","is","python","lists"]
print(a)

# Accessing items
print("\n")
a=["this","is","python","lists"]
print(a[2])

"""For Loop through lists"""
print("\n")
for i in a:
 print(i)

# Negative indexing
print("\n")	
a=["this","is","python","lists"]
print(a[-0])
print("\n")
print(a[-4:-3])
print(a[-4:-2])
print(a[-4:-1])
print(a[-4:])

# Change the item values in lists
print("\n")	
a=["this","is","python","lists"]
a[1]="was"
print(a)

# Check the items in the lists
print("\n")	
a=["this","is","python","lists"]
if "is" in a:
 print("yes")

# Check list length
print("\n")	
a=["this","is","python","lists"]
print(len(a))

# Add items in lists
print("\n")	
a=["this","is","python","lists"]
a.append("hello world")
print(a)

# Insert an item in the position
print("\n")	
a=["this","is","python","lists"]
a.insert(2,"a")
print(a)

# remove the specified items using remove()
print("\n")	
a=["this","is","python","lists"]
a.remove("is")
print(a)

# remove the items using pop() method 
# if the index is not specified it removes the last index
print("\n")	
a=["this","is","python","lists"]
a.pop(1)
print(a)

# remove the items using del() method
print("\n")	
a=["this","is","python","lists"]
del a[1]
print(a)

# clear the lists using clear() method ,it will empty the lists
print("\n")	
a=["this","is","python","lists"]
a.clear()
print(a)

# copy the lists to another values copy()
print("\n")	
a=["this","is","python","lists"]
b= a.copy()
print(b)

#Make the copy of the lists using list()
print("\n")	
a=["this","is","python","lists"]
b= list(a)
print(a)

# Join Two lists 
print("\n")	
a=["this","is",]
b=["python","list"]
c=a+b
print(c)
print(a+b)

# join lists using append() method
a=["this","is",]
b=["python","list"]
for c in b:
 a.append(c)
print(a)

#extend lists using extend()
a=["this","is",]
b=["python"]
a.extend(b)
print(a)

# Construct lists using list(()) method
a=list(("hi","hello"))
print(a)
