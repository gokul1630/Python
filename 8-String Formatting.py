"""
Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning"""


# two types of strings
a="hello word"
b='hello world'

print(a)
print(b)

#Multi line strings 

a="""\nThis 
is 
multiline
string"""

print(a)

# String is an array
 
a="Hello World"

print(a[0]) # Output is 'H'

# String Slicing

a="HiGokul"
print(a[1:5]) #print elements from 1 to 5

# Negative indexing

a="HiGokul"
print(a[-3:-1])

# String length

a="Hi Gokul"
print(len(a))


#String Methods
"""
Strip() - removes any whitespaces in beginning & end of the strings
upper() - converts any lowercase into highercase letters
lower() - converts any highercase into lowercase letters
replace() - replaces the text in strings
split() - This method splits the string into substrings if it finds instances of the separator
"""
# Strip method
a=" hi Gokul "
print(a.strip())

#upper 
a="Gokul"
print(a.upper())

# lower
a="GOKUL"
print(a.lower())

#Split
a="Gokul prasanth"
print(a.split(","))

# replace
a="Gokul"
print(a.replace("G","H"))

""""""""""""""""""""""""
"""Check String"""

a="Gokul"
b= "G" in a
print(b) # returns true

a="Gokul"
b= "G" not in a # not in method returns true into false
print(b) # returns true


"""""""""""""""""""""""""""

string Concatenation
To concatenate, or combine, two strings you can use the + operator."""

a="Gokul"
b="Prasanth"
c=a+b
print(c)
print(a+" "+b) # add space between two strings

"""String Format

string cannot be added into integers but string & number can 
be added by format() method"""

#The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are present

a=20
b="Gokul is {} years old"
print(b.format(a))

#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

a=20
b=19
c=21
d="Gokul is {} years old, Kavihasan is {} years old, lokesh is {} years old"
print(d.format(a,b,c))


#index numbers {0} to be sure the arguments are placed in the correct placeholders

a=20
b=19
c=21
d="Gokul is {1} years old, Kavihasan is {2} years old, lokesh is {0} years old"
print(d.format(a,b,c))



"""Escape Characters"""

# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	HexValue

