from urllib2 import urlopen, Request, URLError
from urllib import quote_plus
import json
from film import Film

api_key = 'c65f2dbe'
base_url = 'http://omdbapi.com/?tomatoes=true'

def get_films_by_title(title):
	url = base_url + '&t=' + quote_plus(title)
	print url
	request = Request(url)
	try:
		response = urlopen(request)
		film = json.loads(response.read())
		print film
		if not film['Response']: return None
		else: return Film(film)
	except URLError, e:
		print 'No filmz :(( got an error code'
		return None

def get_films_by_id(id):
	url = base_url + '&i=' + id
	request = Request(url)
	try:
		response = urlopen(request)
		film = json.loads(response.read())
		if not film['Response']: return None
		else: return Film(film)
	except URLError, e:
		print 'No filmz :(( got an error code'
		return None