def is_paired(input_string):
    """
    checks if open brackets in the input_string have corresponding closing brackets.
    :input_string: str - string containing the text to be checked
    :returns: bool - True if brackets match, else False
    """

    OPEN_BRACKETS = ["(", "[", "{"]
    CLOSE_BRACKETS = [")", "]", "}"]
    
    brackets_stack = []
    for letter in input_string:
        if letter in OPEN_BRACKETS:
            brackets_stack.append(OPEN_BRACKETS.index(letter))
        if letter in CLOSE_BRACKETS:
            try:
                if letter != CLOSE_BRACKETS[brackets_stack.pop()]:
                    return False
            except:
                return False
                
    return (len(brackets_stack) == 0)
