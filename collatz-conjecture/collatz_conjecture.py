def check_even(number):
    return (number % 2 == 0)
    
def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    
    count = 0
    while number > 1:
        if check_even(number):
            number = number / 2
        else:
            number = 3 * number + 1
        count += 1

    return count
