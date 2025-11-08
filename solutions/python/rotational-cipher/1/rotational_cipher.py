def rotate(text, key):
    ciper_text = ''
    #65 - 90 for (A-Z)
    #97 - 122 for (a-z)
    for c in text:
        # check character is alphabet
        int_value = ord(c)
        ciper_int_value = int_value + key
        #lower-case
        if 65<=int_value<=90:
            if ciper_int_value > 90:
                ciper_int_value = 64+(ciper_int_value - 90)
            ciper_text += chr(ciper_int_value)
        #upper-case
        elif 97<=int_value<=122:
            if ciper_int_value > 122:
                ciper_int_value = 96+(ciper_int_value - 122)
            ciper_text += chr(ciper_int_value)
        else:
            ciper_text += c
    return ciper_text

