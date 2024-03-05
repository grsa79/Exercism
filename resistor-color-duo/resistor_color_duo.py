COLOR_CODE = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

def color_code(color: str) -> int:
    """
    returns the value coded by an individual color band
    taken from my solution of resistor_color - exercise...
    :color: str - color of the band
    :returns: int - corresponing number
    """
    try:
        return COLOR_CODE.index(color)
    except:
        raise ValueError("no valid color given")
    
def value(colors: list) -> int:
    """ 
    returns resistor value coded by two color bands
    :colors - str color1-color2
    :returns int: resistance value 10*color1 + color2
    """
    return 10*color_code(colors[0]) + color_code(colors[1])
