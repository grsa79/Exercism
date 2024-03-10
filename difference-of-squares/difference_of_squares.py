def square_of_sum(number: int) -> int:
    """
    sums up all integers up to number and squares the result
    :number - int
    :returns - int
    """
    return pow(sum(i for i in range(number+1)),2)


def sum_of_squares(number: int) -> int:
    """
    squares all integers up to number and sums the results
    :number - int
    :returns - int
    """
    return sum(pow(i, 2) for i in range(number + 1))


def difference_of_squares(number: int) -> int:
    """
    calculates the difference between sq of sum and sum of sq
    """
    return square_of_sum(number) - sum_of_squares(number)
