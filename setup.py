from setuptools import setup
setup(
    name='movie-app-cli',
    version='0.1.0',
    packages=['movie_app_cli'],
    install_requires=[
    	'Click',
    	'requests'
    ],
    entry_points={
    "console_scripts":[
        'hello=movie_app_cli.__main__:cli',
        'getinfo=movie_app_cli.get_rating:cli',
        'searchShow=movie_app_cli.search_show:cli'
        ]
      }
    )