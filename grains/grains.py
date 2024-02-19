def square(number):
    if number not in range(1,65):
        raise ValueError("square must be between 1 and 64")
    
    grain_count = 1
    for sq in range(1, number):
        grain_count *=2

    return grain_count

def total():
    return sum(square(index) for index in range(1,65))
