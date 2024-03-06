COLOR_CODE = ["black", "brown", 
              "red", "orange", 
              "yellow", "green", 
              "blue", "violet", 
              "grey", "white"]

COLOR_TOLERANCE = [("grey", " ±0.05%"),
                   ("violet", " ±0.1%"),
                   ("blue", " ±0.25%"),
                   ("green", " ±0.5%"),
                   ("brown", " ±1%"),
                   ("red", " ±2%"),
                   ("gold", " ±5%"),
                   ("silver", " ±10%")]


def color_code(color: str) -> int:
    """
    returns the value coded by an individual color band
    :color: str - color of the band
    :returns: int - corresponing number
    taken from solution of "resistor-color"
    """
    if not color in COLOR_CODE: raise ValueError("no valid color given")
    return COLOR_CODE.index(color)


def tolerance_code(color: str) -> str:
    """
    returns the tolerance value coded by an individual color band as str: +- x%
    :color: str - color of the band
    :returns: str - corresponing tolerance
    """
    for (col_str, tol_str) in COLOR_TOLERANCE:
        if col_str == color: return tol_str


def resistor_label(colors):
    """
    gives resistance value in ohms or kohms
    :colors: list of str - colors of the bands in order
    :returns: str - resistance value and unit
    """
    bands = len(colors)
    if bands == 1:
         return str(color_code(colors[0])) + " ohms"
    if bands == 4:
        value = color_code(colors[0])*10 + color_code(colors[1])
        zeros = color_code(colors[2])
    if bands == 5:
        value = color_code(colors[0])*100 + color_code(colors[1])*10 + color_code(colors[2])
        zeros = color_code(colors[3])

    value = value * pow(10, zeros)

    if value < 1_000:
        if value == int(value): value = int(value)
        return str(value) + " ohms" + tolerance_code(colors[-1])
    if value < 1_000_000:
        value = value / 1000
        if value == int(value): value = int(value)
        return str(value) + " kiloohms" + tolerance_code(colors[-1])
    if value < 1_000_000_000:
        value = value / 1_000_000
        if value == int(value): value = int(value)
        return str(value) + " megaohms" + tolerance_code(colors[-1])
    value = value / 1_000_000_000
    if value == int(value): value = int(value)
    return str(value) + " gigaohms" + tolerance_code(colors[-1])

