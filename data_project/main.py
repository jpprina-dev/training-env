import click


@click.command()
@click.option('--hello', prompt=True)
def main(hello):
    if hello:
        click.echo(f'Hello {hello}!')


if __name__ == "__main__":
    main()