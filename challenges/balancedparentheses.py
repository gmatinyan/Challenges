"""Does a string have balanced parentheses?

For example::

   >>> has_balanced_parens("()")
   True

   >>> has_balanced_parens("(Oh Yes)")
   True

   >>> has_balanced_parens("(Oh Noes!)(")
   False

   >>> has_balanced_parens("((There's a bonus open paren here.)")
   False

   >>> has_balanced_parens(")")
   False

   >>> has_balanced_parens("(")
   False

   >>> has_balanced_parens("(This has (too many closes.) ) )")
   False

If you receive a string with no parentheses, consider it balanced::

   >>> has_balanced_parens("Hey...there are no parens here!")
   True
"""


def has_balanced_parens(phrase):
    """Does a string have balanced parentheses?"""

    count = 0

    for char in phrase:
      if char == "(":
        count += 1
      elif char == ")":
        count -= 1

        if count < 0:
          return False

    if count == 0:
      return True
    else:
      return False
  
    # parens = []
    # for char in phrase:
    #   if char == "(":
    #     parens.append(char)
        
    #   elif char == ")" and len(parens) > 0:
    #     parens.pop()
          
    #   elif char == ")":
    #     return False  
             
    # if len(parens) > 0:
    #   return False
    # else:
    #   return True





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY PARENS!\n"
