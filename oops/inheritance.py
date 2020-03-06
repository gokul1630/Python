class gp:
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def pg(self):
		print(self.name,self.age)
class my(gp):
	def __init__(self, name,age,year):
    		super().__init__(name,age)
    		self.year=year
	def pri(self):
    	    print(self.name,self.age,self.year)
x=my("gokul",20,2020)
x.pri()
