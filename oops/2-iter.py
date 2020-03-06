class nums:
	def __iter__(self):
		self.a=0
		return self
	def __next__(self):
		if self.a <=30:
			x=self.a
			self.a+=1
			return x
		else:
		 raise StopIteration	
obj=nums()
itr=iter(obj)
for i in itr:
	print(i)