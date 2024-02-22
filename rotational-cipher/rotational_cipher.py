from string import ascii_lowercase, ascii_uppercase

def rotate(text, key):
    """
    ciphering a given text with rotational cipher
    :text: - str literal containing text
    :key: - str containing cipher-Key: ROT+Nr
    :returns: - str, containing Ciphertext
    """

    #Dealing with the key:
    key = key % 26

    # making cipher-table
    cipher_table = []
    for index in range(25, -1, -1):
        cipher_table.append((ascii_lowercase[index], (ascii_lowercase + ascii_lowercase)[index + key]))
        cipher_table.append((ascii_uppercase[index], (ascii_uppercase + ascii_uppercase)[index + key]))

    #print(cipher_table)
    cipher_text = ""
    for letter in text:
        for (old, new) in cipher_table:
            if letter == old:
                cipher_text = cipher_text + new
        if not (letter in ascii_lowercase + ascii_uppercase):
            cipher_text = cipher_text + letter

    return cipher_text