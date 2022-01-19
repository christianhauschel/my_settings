from rich import print

def pretty_print(txt:str, type:str="section") -> None:
    """
    Pretty prints of sections and subsections into the command line.
    """
    if type == "section":
        print("\n\n================================================================================")
        print(f"    {txt.upper()}")
        print("================================================================================")
    elif type == "subsection":
        print("\n----------------------------------------")
        print(f"    {txt}")
        print("----------------------------------------")
    elif type == "subsubsection":
        print(f"\n--- {txt} ---")