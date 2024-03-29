from rich import print
from rich.style import Style
from rich.text import Text
from rich.panel import Panel
from rich import box
from rich.console import Console


def print_exception(show_locals=True, **kwargs):
    console = Console()
    console.print_exception(show_locals=show_locals, **kwargs)


def pretty_print(txt: str, type: str = "section", simple=False) -> None:
    """Pretty prints of sections and subsections into the command line.

    Parameters
    ----------
    txt : str
        text to print
    type : str, optional
        section type, by default "section",
        other options: "subsection", "subsubsection"
    """

    if type == "section":
        if simple:
            print(Text("Test", soft_wrap=True))
            print(
                Text(
                    "\n\n================================================================================"
                )
            )
            print(f"    {txt.upper()}")
            print(
                "================================================================================"
            )
        else:
            print()
            print()
            print(
                Panel(
                    Text(txt.upper(), justify="center"),
                    style=Style(bold=True),
                    box=box.DOUBLE,
                    padding=0,
                    width=80,
                )
            )
    elif type == "subsection":
        if simple:
            print("\n----------------------------------------")
            print(f"    {txt}")
            print("----------------------------------------")
        else:
            print()
            print(
                Panel(
                    Text(txt, justify="center"),
                    style=Style(bold=False),
                    box=box.SQUARE,
                    width=80,
                )
            )
    elif type == "subsubsection":
        if simple:
            print(f"\n--- {txt} ---")

        else:
            print()
            print(
                Panel(
                    Text(txt, justify="center"),
                    style=Style(bold=False),
                    box=box.HORIZONTALS,
                    width=40,
                )
            )
