import click
from flask.cli import with_appcontext


@click.command(name='hello', help='Print hello message')
@click.option('-n', '--name', default='', help='The person to greet.')
@with_appcontext
def hello(name):
    print(f'hello {name}')
