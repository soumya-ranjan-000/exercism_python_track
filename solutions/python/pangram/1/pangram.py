#a sentence is a pangram if it contains each of the 26 letters
#in the English alphabet.
def is_pangram(sentence):
    sentence = sentence.lower()
    for letter in range (97,123):
        if chr(letter) not in sentence:
            print('char not found: '+chr(letter))
            return False
    return True