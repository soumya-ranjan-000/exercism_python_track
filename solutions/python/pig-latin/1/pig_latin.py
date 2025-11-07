def translate(text):
    words = text.split()
    translated = [translate_word(word) for word in words]
    return ' '.join(translated)

def translate_word(word):
    # Rule 1: words beginning with vowel sounds or 'xr' or 'yt'
    if word[0] in 'aeiou' or word.startswith(('xr', 'yt')):
        return word + 'ay'
    
    # Find the index where consonant cluster ends
    i = 0
    length = len(word)
    
    while i < length:
        # Rule 3: handle 'qu' case
        if i + 1 < length and word[i:i+2] == 'qu':
            i += 2
            break
            
        # Rule 4: handle consonant + 'y' case
        if word[i] == 'y' and i > 0:
            break
            
        # Rule 2: continue for consonants
        if word[i] not in 'aeiou':
            i += 1
        else:
            break
    
    # Handle special case where 'qu' follows consonant(s)
    if i < length - 1 and word[i:i+2] == 'qu':
        i += 2
        
    return word[i:] + word[:i] + 'ay'