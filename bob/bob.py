def response(hey_bob):
    
    is_yelled = False
    if str.isupper(hey_bob):
        is_yelled = True
    
    #is_question = False
    #if hey_bob.find("?") >= 0:
    #    is_question = True
    is_question = hey_bob.strip().endswith("?")

    is_silent = False
    if hey_bob.strip() == "":
        is_silent = True
    
    if is_yelled:
        if is_question:
            return "Calm down, I know what I'm doing!" 
        else:
            return "Whoa, chill out!"
    
    if is_question:
        return "Sure."
    if is_silent:
        return "Fine. Be that way!"
    
    return "Whatever."
