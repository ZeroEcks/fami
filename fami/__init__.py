import sys
import click
from fami.archive import run_archive
from fami.instagram import run_instagram

if sys.version_info < (3, 12):
    raise ImportError(
        f'You are using an unsupported version of Python. Only Python versions 3.12 and above are supported by fami')


@click.group()
def cli():
    pass


@click.command()
@click.argument('output-path', type=click.Path(
    exists=True,
    file_okay=False,
    dir_okay=True,
    resolve_path=True)
)
def archive(output_path):
    click.echo("Archive")
    run_archive(output_path)


cli.add_command(archive)


@click.command()
def google_photos():
    click.echo("Google photos")
    pass


cli.add_command(google_photos)


@click.command()
def instagram():
    click.echo("Instagram")
    run_instagram()


cli.add_command(instagram)
