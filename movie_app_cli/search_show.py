import requests
api_url = "http://api.tvmaze.com/search/shows?q="
import click
import json

@click.command()
@click.argument('show_name')
def cli(show_name):
	data = requests.get(api_url+show_name)
	print("this is api + url",api_url+show_name)
	data = data.text
	data = json.loads(data)

	for i in data:
		show = i['show']
		rating = show['rating']
		average = rating['average']
		print("Title: " + show['name'])
		print("Rating: %s" %average)
		print("Premier Date: %s" %show['premiered'])
		print("\n")
if __name__ == '__main__':
	cli()