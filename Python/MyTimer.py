import time as t

class MyTime():
	def __str__(self):
		return self.prompt
	__repr__ = __str__
	
	def start(self):
		self.start = t.localtime()
		print("Start timeing:")

	def stop(self):
		self.stop = t.localtime()
		print("Ending timeing.")


	def _calc(self):
		self.lasted = []
		self.prompt = "The whole running time is:"
		for index in range(6):
			self.lasted.append(self.stop[index]-self.start[index])
			self.prompt += str(lasted[index])