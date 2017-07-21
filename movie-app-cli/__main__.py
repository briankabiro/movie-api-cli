import click

@click.command()
@click.option("--name",help="name of the tv show")
@click.argument('name')
def cli(name):
	print("hello world %s" %name)

if __name__ == '__main__':
	cli()