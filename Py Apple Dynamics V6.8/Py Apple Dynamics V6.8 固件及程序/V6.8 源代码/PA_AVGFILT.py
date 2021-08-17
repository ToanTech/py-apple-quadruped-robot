class avg_filiter():
	def __init__(self,cache_data):
		self.cache = cache_data
		self.len = len(cache_data)
		self.cache[0] = self.len
		self.sum = 0
		for item in cache_data[3:]:
			self.sum += item
		self.cache[1] = self.sum
		
	def avg(self,new_data):
		self.cache[1] = self.cache[1] - self.cache[3]
		self.cache[1] = self.cache[1] + new_data
		self.cache[3:-1] = self.cache[4:]
		self.cache[-1] = new_data
		return self.cache[1]//(self.len - 3)

