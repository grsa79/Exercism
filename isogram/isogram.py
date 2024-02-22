from string import ascii_lowercase

def is_isogram(string):
    """
    checks, wether the word in the input-string has no repeating letters.
    :string:str - contains word to be checked
    :returns: bool - True if the input string contains an isogram, else false
    """
    for letter in ascii_lowercase:
        if str.lower(string).count(letter)>1:
            return False
    return True
    
