import collections

#TODO add more pertinent fields (score, etc, corrected film name)
class FilmRequest(object):
	def __init__(self, priority, query):
		self.priority = priority
		self.query = query

	def __cmp__(self, other):
		return cmp(self.priority, other.priority)

class NetflixList():
	def __init__(self):
		self.films = {}

	def add(self, priority, query):
		self.films[query] = FilmRequest(priority, query)
		self.films = collections.OrderedDict(sorted(self.films.items(), key=lambda f: f[1].priority))

	def delete(self, query):
		if query in self.films:
			del self.films[query]
		else:
			print 'Film wasn\'t present in list!' #TODO have bot send this

	def empty(self):
		return len(self.films) == 0

	def pop(self):
		if self.empty():
			return None
		else:
			return self.films.popitem()

	def get(self, n):
		return list(self.films.values())[:n]

nl = NetflixList()

nl.add(142, 'Good WillHunting')
nl.add(5, 'The Shining')
nl.add(3, 'Taken')
nl.add(3, 'Good WillHunting 2')
nl.add(14, 'The Shining 2')
nl.add(10, 'Taken 2')



