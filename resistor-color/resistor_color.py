COLOR_CODE = ["black", "brown", 
              "red", "orange", 
              "yellow", "green", 
              "blue", "violet", 
              "grey", "white"]


def color_code(color: str) -> int:
    """
    returns the value coded by an individual color band
    :color: str - color of the band
    :returns: int - corresponing number
    """
    if not color in COLOR_CODE: raise ValueError("no valid color given")
    return COLOR_CODE.index(color)
    

def colors() -> list:
    """
    lists all possible color bands
    """
    return COLOR_CODE