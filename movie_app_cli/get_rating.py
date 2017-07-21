import requests
import json
single_show_api_url = "http://api.tvmaze.com/singlesearch/shows?q="
import click

@click.command()
@click.argument('show_name')
def cli(show_name):
	data = requests.get(single_show_api_url + show_name)
	data = data.text
	data = json.loads(data)
	rating = data['rating']
	rating = rating['average']
	print("%s has a rating of %s" %(show_name,rating))

if __name__ == '__main__':
	cli()