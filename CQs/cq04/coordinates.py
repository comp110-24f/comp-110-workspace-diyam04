""""Printed format from two string inputs"""

_author_ = "730669985"

def get_coords(xs: str, ys: str) -> None:
    """Print formatted pairs of characters from the two input strings."""
    for x in xs:
        for y in ys:
            print(f"({x},{y})")