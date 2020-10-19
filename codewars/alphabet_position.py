"""In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc."""

def alphabet_position(text):
    alphabet_values = dict((v,k) for k,v in dict(enumerate('abcdefghijklmnopqrstuvwxyz')).items())
    return " ".join([str(alphabet_values[i]+1) for i in text.lower() if i in 'abcdefghijklmnopqrstuvwxyz'])

"""
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
"""