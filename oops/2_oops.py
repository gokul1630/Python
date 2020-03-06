class gp:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def meth(self):
		print(self.name,self.age)
obj=gp('gokul',20)
obj.meth()	
