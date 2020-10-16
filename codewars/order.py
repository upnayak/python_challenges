"""
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
"""

import re
def order(sentence):
  sentence = sentence.split(" ")
  if sentence[0] == '':
      return ''
  sentence_dict = {int(re.search(r'[1-9]', alpha).group(0)) : alpha for alpha in  sentence}
  return " ".join([sentence_dict[x] for x in sorted(sentence_dict.keys())])
