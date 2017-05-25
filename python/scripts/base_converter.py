from math import log, floor

"""Convert input into specified base. Assumes input is in base 10!

   Imagine base notation represented by columns that are zero-indexed
   from right-to-left where column i represents base ** i, like this:

   Column:    |   i    |   3    |   2    |   1    |   0    |
   Exponent:  | 2 ** i | 2 ** 3 | 2 ** 2 | 2 ** 1 | 2 ** 0 |
   Value:     | 2 ** i |   8    |   4    |   2    |   1    |

   Method uses floor(log(x/base)) to calculate i, then loops over the
   "columns" from i to zero. On each loop, the method calculates what
   digit(s) should be written in the column and how much of x remains
   to be converted.
"""
def convert_to_base(x, base):
  if base <= 0:
    print "\nERROR - base must be greater than zero\n"
    return

  if x == 0:
    return 0

  result = ''
  remainder = abs(x)
  exponent = int(floor(log(abs(x),base)))

  while exponent >= 0:
    units = base ** exponent
    if remainder >= units:
      (q, remainder) = divmod(remainder, units)
      result = result + str(q)
    else:
      result = result + '0'

    # Proceed to next column
    exponent = exponent -1

  return -1 * int(result) if x < 0 else int(result) 
