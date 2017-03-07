class Movie:
	def __init__(self, name, director = None, gender = ""):
		self.name = name
		self.director = director
		self.gender = gender
		
	def get_name():
		return self.name
	
	def get_director():
		return self.director
		
	def get_gender():
		return self.gender
		
class Director:
	def __init__(self, name):
		self.name = name
	
	def get_name():
		return self.name

