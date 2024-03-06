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
    taken from solution of "resistor-color"
    """
    if not color in COLOR_CODE: raise ValueError("no valid color given")
    return COLOR_CODE.index(color)


def label(colors: list) -> str:
    """
    gives resistance value in ohms or kohms
    :colors: list of str - colors of the bands in order
    :returns: str - resistance value and unit
    """
    value = color_code(colors[0])*10 + color_code(colors[1])
    zeros = color_code(colors[2])
    if value % 10 == 0:
        value = int(value/10)
        zeros += 1
    if zeros < 3:
        return str(value * pow(10, zeros)) + " ohms"
    if zeros < 6:
        return str(value * pow(10, zeros-3)) + " kiloohms"
    if zeros < 9:
        return str(value * pow(10, zeros-6)) + " megaohms"
    return str(value * pow(10, zeros-9)) + " gigaohms"
