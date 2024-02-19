def square_root(number):
    """
    not using math.sqrt() or pow(number, 1/2) - but a numerical approach known as the Heron's method.
    I adopted it by rounding to the fact, that in this exercise only natural numbers are solutions. 
    :param number: int - pos. number, of which the square root is to be calculated.
    :returns : int - square root of the given number.
    """
    root_est = 1.
    while round(root_est) != number / round(root_est):
        root_est = (root_est + number / root_est)/2

    return round(root_est)

