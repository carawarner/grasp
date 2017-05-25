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

from math import log, floor

def convert_to_base(num, base):
    """Rewrite a base 10 num in base specified by input"""
    if base <= 0:
        print "\nERROR - base must be greater than zero\n"
        return

    if num == 0:
        return 0

    result = ''
    remainder = abs(num)
    exponent = int(floor(log(abs(num), base)))

    while exponent >= 0:
        units = base ** exponent
        if remainder >= units:
            (quotient, remainder) = divmod(remainder, units)
            result = result + str(quotient)
        else:
            result = result + '0'

        # Proceed to next column
        exponent = exponent -1

    return -1 * int(result) if num < 0 else int(result)

def try_base_converter():
    """Provide a way to interact with base_converter from the CL"""
    num = input("\nWhat number would you like to convert? ")
    base = input("Into which base? ")
    result = convert_to_base(num, base)

    if isinstance(result, int):
        print "\nIn base %d the number %d is represented by %d\n" % (base, num, result)
    else:
        print "Result that came back wasn't an integer. Something went wrong."

try_base_converter()
