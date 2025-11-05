import click

from ..handlers.resources.frontend import FrontendHander


@click.group(help="The Executable Intelligence Platform")
def kx():
    pass


@click.command(help="Initiate kickoff")
@click.option("--enable_backend", is_flag=True, default=False, help="Enables Rust backend")
def start(enable_backend):
    if enable_backend:
        print("Rust Backend Enabled")
        from backend import sum_as_string

        print(sum_as_string(1, 2))
    else:
        FrontendHander().init_frontend()


kx.add_command(start)


def cli() -> None:
    kx()
