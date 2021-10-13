def pretty_print(txt:str, type:str="section") -> None:
    if type=="section":
        print("\n\n================================================================================")
        print(f"    {txt.upper()}")
        print("================================================================================")
    if type=="subsection":
        print("\n----------------------------------------")
        print(f"    {txt}")
        print("----------------------------------------")
    if type=="subsubsection":
        print(f"\n--- {txt} ---")