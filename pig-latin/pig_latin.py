consonant = ["thr", "sch", "ch", "qu", "th",
             "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n",
                 "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

vowel = ["a", "e", "i", "o", "u", "xr", "yt"]

def check_vowel(single_word):
    """
    checks if a word starts with vowel sound and translates it
    :return: str, bool - translated word, is_translated-flag
    """
    global vowel
    for letter in vowel:
        if single_word.startswith(letter):
            return (single_word + "ay", True)
    return("", False)

def check_consonant(single_word):
    """
    checks if a word starts with consonant sound and translates it
    :return: str, bool - translated word, is_translated-flag
    """
    global consonant
    for letter in consonant:
        if single_word.startswith(letter):
            prefix = letter
            if single_word.startswith(letter + "qu"):
                prefix = prefix + "qu"    
            return (single_word.removeprefix(prefix) + prefix + "ay", True)
    return("", False)

def check_y(single_word):
    """
    checks special rules for words containing ys
    :return: str, bool - translated word, is_translated-flag
    """
    if (len(single_word)==2 and single_word[1]=="y"):
        return("y"+single_word[0] + "ay", True)
    
    index = single_word.find("y")
    if 0 < index <len(single_word)-1:
        prefix = single_word[:index]
        return (single_word.removeprefix(prefix)+prefix+"ay", True)
    return ("", False)

def translate(text):
    text_list = text.split()
    for index, word in enumerate(text_list):
        is_translated = False
        translated_word = ""
        (translated_word, is_translated) = check_y(word)
        if not is_translated:
            (translated_word, is_translated) = check_vowel(word)

        if not is_translated:
            (translated_word, is_translated) = check_consonant(word)

        text_list[index] = translated_word      
    
    return " ".join(text_list)
