import requests
import json
api_url = "http://api.tvmaze.com/search/shows?q="
single_show_api_url = "http://api.tvmaze.com/singlesearch/shows?q="

def test_api_is_up():
	show = 'arrow'
	data = requests.get(api_url + show)
	assert(data.status_code == 200)

def test_shows_are_returned():
	show = "flash"
	data = requests.get(api_url + show)
	assert(len(data.text) != 0) 

def test_return_single_show():
	''' test if the api returns a single result '''
	show = "gotham"
	data = requests.get(single_show_api_url + show)
	assert(data.text)

def test_return_rating():
	show = "girls"
	data = requests.get(single_show_api_url + show)
	data = data.text
	data = json.loads(data)
	rating = data['rating']
	rating = rating['average']
	assert(isinstance(rating, float) == True)
	

