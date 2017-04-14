import urllib3
import json
from .film import Film

api_key = 'c65f2dbe'
base_url = 'http://omdbapi.com/?tomatoes=true'

def get_film_by_title(title):
	url = base_url
	print(url)
	http = urllib3.PoolManager()
	r = http.request('GET', url + "&t=" + title.replace(" ", "+"))
	try:
		response = r.data
		film = json.loads(response.decode('utf-8'))
		print(film)

		if film['Response'] == 'False': return None
		else: return Film(film)
	except URLError:
		print('No filmz :(( got an error code')
		return None

def get_film_by_id(id):
	url = base_url + '&i=' + id
	http = urllib3.PoolManager()
	r = http.request('GET', url)
	try:
		response = r.data
		film = json.loads(response.decode('utf-8'))
		if not film['Response']: return None
		else: return Film(film)
	except URLError:
		print('No filmz :(( got an error code')
		return None