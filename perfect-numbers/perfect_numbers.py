

def factors(number: int):
    """
    determines factors of the given number
    :param number: int - a positive integer
    :return: list of int - prime factors of the given number
    """
    factorList = []
    for no in range(1, number):
        if number % no == 0:
            factorList.append(no)
    return factorList

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if isinstance(number, int) == False or number < 1: 
        raise ValueError("Classification is only possible for positive integers.")
    
    summe = sum(factors(number))
    
    if number == summe:
        return("perfect")
    if number < summe:
        return("abundant")
    return("deficient")
    