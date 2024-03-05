"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
SUBLIST = -1
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 0

def sublist(list_one : list[any], list_two : list[any]) -> int:
    """
    checks if a list A is sublist, superlist or equal to a list B

    :list_one, list_two two lists to be compared
    :returns int according to findings...
    """
    list_one_length = len(list_one)
    list_two_length = len(list_two)

    # taking care of empty lists
    if list_one_length == 0 and list_two_length >0: return SUBLIST
    if list_two_length == 0 and list_one_length > 0: return SUPERLIST

    # equal?
    if list_one == list_two: return EQUAL
    
    # superlist, i.e. list_two is in list_one?
    if list_one_length > list_two_length:
        for one_index in range(list_one_length - list_two_length+1):
            if list_one[one_index: one_index+list_two_length] == list_two: return SUPERLIST
    
    # sublist, i.e. list_one is in list_two - same as before, but switched lists?
    if list_one_length < list_two_length:
        for two_index in range(list_two_length - list_one_length+1):
            if list_two[two_index: two_index+list_one_length] == list_one: return SUBLIST
    
    return UNEQUAL


