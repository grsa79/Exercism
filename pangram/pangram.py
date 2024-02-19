def is_pangram(sentence):
    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    sentence = str.lower(sentence)

    for letter in abc:
        if sentence.find(letter) < 0:
            return False
    return True