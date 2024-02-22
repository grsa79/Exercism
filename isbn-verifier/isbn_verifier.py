def is_valid(isbn):
    """
    ISBN-10: d1 - d2 d3 d4 - d5 d6 d7 d8 d9 - d10
    check, whether the supplied string is a valid ISBN-10 using the check-formula
    (d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11 == 0
    dashes may be omitted
    d10 might be 10 which is represented by X

    :isbn: - str, containing string to be checked
    :returns: - bool, True if string is valid ISBN
    """
    check_sum = 0

    #removing potential dashes & checking for correct number of digits
    isbn = str.replace(isbn, "-", "")
    if len(isbn) != 10:
        return False 
    
    # dealing with the check-digit 
    if isbn[-1] == "X":
        check_sum = 10
    else:
        try:
            check_sum = int(isbn[-1])
        except:
            return False
    
    # converting isbn-string to digit-ints and calculating checksum
    for index in range(0, 9):
        try:
            check_sum = check_sum + (10-index) * int(isbn[index])
        except:
            return False
    return (check_sum % 11 == 0)
    

         
    