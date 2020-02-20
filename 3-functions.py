x = "aw"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("P is " + x)



def myfunc():
  global x
  x = "fan"

myfunc()

print("Python " + x)



x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Py is " + x)


