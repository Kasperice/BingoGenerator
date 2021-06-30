from bingo import BingoGenerator
import click


@click.group()
def cli():
    pass


@click.command()
@click.option('--language', default="en", help="Choose lector language")
def start(language: str):
    bingo = BingoGenerator(language=language)
    bingo.start_game()


cli.add_command(start)

if __name__ == '__main__':
    cli()
