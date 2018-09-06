def hasAnE(word):
  """
  return True when word is a string that contains the letter 'E' 
  (and no letter 'e')
  It should work both for lower and upper case.
  When word isn't a string, return False (because there is no
  such thing as an E inside a number, for example)
  """

  if type(word) != str:
    return False

  # we know if we got this far that word is a str

  i = 0
  while i < len(word):
    current_char = word[i]
    if current_char == "E" or current_char == "e":
      return True

    i += 1

  # if I got here, I know there was no E/e in the string
  return False

# return True if we get a tuple filled with nothing but strings
# of length 3, False otherwise
def tupleContainingStringsOfLength3(t):
  if type(t) != tuple:
    return False

  # we know if we got this far that t is a tuple

  i = 0
  while i < len(t):
    current_elem = t[i]
    if type(current_elem) == str and len(current_elem) == 3:
      # this is good, continue
      # notice YOU CAN'T RETURN TRUE HERE
      pass
    else:
      # this is bad
      return False

    i += 1

  # if I got here, I know that nothing was wrong
  return True

