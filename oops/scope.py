def fun():
	a="hello"
	print(a)
fun()	


def fun():
	a=30
	def inrfun():
		print(a)
	inrfun()
fun()		


def fun():
	global x #global variable
	x=300
fun()	
print(x)