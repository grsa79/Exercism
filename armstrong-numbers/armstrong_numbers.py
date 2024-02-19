def is_armstrong_number(number):
    num_string = str(number)
    return sum(int(Ziffer[1]) ** (len(num_string)) for Ziffer in enumerate(num_string)) == number
