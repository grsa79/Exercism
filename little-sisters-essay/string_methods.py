"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed.

    :param title: str - title string that needs title casing.
    :return: str - title string in title case (first letters capitalized).
    
    My first solution - as I did not realize there's a method "title", but used "capitalize" - 
    looked like that:

    words_in_sentence = str.split(title)
    capital_title = []
    for word in words_in_sentence:
        capital_title.append(str.capitalize(word))

    title =""
    for word in capital_title:
        title +=word + " "
 
    return clean_up_spacing(title)

    however, the following is much clearer:
    """
    return str.title(title)
    

def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present.

    :param sentence: str - a sentence to check.
    :return: bool - return True if punctuated correctly with period, False otherwise.
    """

    return str.endswith(clean_up_spacing(sentence), ".")


def clean_up_spacing(sentence):
    """Verify that there isn't any whitespace at the start and end of the sentence.

    :param sentence: str - a sentence to clean of leading and trailing space characters.
    :return: str - a sentence that has been cleaned of leading and trailing space characters.
    """ 
    return str.strip(sentence)


def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    :param sentence: str - a sentence to replace words in.
    :param old_word: str - word to replace.
    :param new_word: str - replacement word.
    :return: str - input sentence with new words in place of old words.
    """

    return str.replace(sentence, old_word, new_word)
