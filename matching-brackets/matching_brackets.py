def is_paired(input_string):
    OPEN_BRACKETS = ["(", "[", "{"]
    CLOSE_BRACKETS = [")", "]", "}"]
    
    #needs_break = False
    #needed_brackets = []
    brackets_stack = []
    for letter in input_string:
        if letter in OPEN_BRACKETS:
            brackets_stack.append(OPEN_BRACKETS.index(letter))
        if letter in CLOSE_BRACKETS:
            if len(brackets_stack) == 0:
                return False
            if letter == CLOSE_BRACKETS[brackets_stack[-1]]:
                brackets_stack.pop()
            else:
                return False
                
    return (len(brackets_stack) == 0)
