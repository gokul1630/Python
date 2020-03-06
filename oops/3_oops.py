class gp:
	def __init__(go,name,age):
		go.name=name
		go.age=age
	def fun(abc):
		print(abc.name,abc.age)
obj=gp('gokul',20)
obj.name='prasanth' #change the object properties
obj.fun()