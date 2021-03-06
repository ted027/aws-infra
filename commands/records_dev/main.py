import click
import os
from . import deploy, update, write

abspath = os.path.abspath(__file__)
while not os.path.exists('.git'):
    abspath = os.path.dirname(abspath)
    os.chdir(abspath)

@click.group()
@click.pass_context
def handle(ctx):
    pass

handle.add_command(deploy.deploy)
handle.add_command(update.update)
handle.add_command(write.write)