class gp:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def fun(self):
		print(self.name)
obj=gp('gokul',20)
del obj.age
obj.fun()

print(obj.age) #shows error