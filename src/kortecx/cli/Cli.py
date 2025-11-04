import click
from backend import sum_as_string


@click.group(help="The Executable Intelligence Platform")
def kx():
    pass


@click.command(help="Initiate kickoff")
@click.option(
    "--enable_backend", is_flag=True, default=False, help="Enables Rust backend"
)
def start(enable_backend):
    if enable_backend:
        print("Rust Backend Enabled")
    else:
        print("Using Python Backend")
        print(sum_as_string(1, 2))


kx.add_command(start)


def main() -> None:
    kx()
