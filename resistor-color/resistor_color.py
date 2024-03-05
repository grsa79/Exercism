COLOR_CODE = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

def color_code(color: str) -> int:
    """
    returns the value coded by an individual color band
    :color: str - color of the band
    :returns: int - corresponing number
    """
    try:
        return COLOR_CODE.index(color)
    except:
        raise ValueError("no valid color given")

def colors() -> list:
    """
    lists all possible color bands
    """
    return COLOR_CODE
