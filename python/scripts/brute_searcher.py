# pylint: disable=no-else-return
"""Adapted from an exercise in "Coding the Matrix". This script ingests
a text file, produces an index of the words in that text file, and allows
a user to search that index for one of more words. Validation is minimal.
"""

from string import punctuation

def make_inverse_index(strlist):
    """Take a list containing lines of text and build a dictionary that
    maps every word of every line to a list of the line numbers on which
    it appears.
    """
    index = {}

    for i in range(1, len(strlist)):
        line = sanitize(strlist[i])
        words = line.split(' ')

        for word in words:
            if word == '':
                continue
            if word in index:
                index[word].add(i)
            else:
                index[word] = {i}

    return index


def sanitize(str_to_sanitize):
    """Remove punctuation and line endings. Standardize case."""
    return str_to_sanitize.translate(None, punctuation + '\n').lower()


def search(index, query, operator='OR'):
    """Take a list of search terms and return a set containing the line
    numbers where all (output='AND') or some (output='OR') of the terms
    can be found.
    """
    values = []
    sanitized_input = []
    for term in query:
        sanitized_input.append(sanitize(term))

    for term in sanitized_input:
        if term in index:
            values.append(index[term])
        elif operator == 'AND':
            return [] #Shortcircuit since AND can't be satisfied.

    if len(values) < 1:
        return []
    elif len(values) == 1:
        return values[0]

    if operator.upper() == 'AND':
        return values[0].intersection(*values[1:])
    else:
        return values[0].union(*values[1:])


def sorted_search(index, query, operator='OR'):
    """Convert search() results to a list and return it sorted."""
    values = search(index, query, operator)
    values = [x for x in values]
    values.sort()

    return values

def try_brute_search():
    """Provide a way to interact with vulgar_search from the CL."""
    query = []

    while True:
        term = str(raw_input("Add a search term (if you're done just hit enter): "))
        if term == '':
            break

        query.append(term)

    text = open('src/leaves.txt')
    strlist = text.readlines()
    index = make_inverse_index(strlist)

    union = sorted_search(index, query, 'OR')

    if union:
        print "\nLINES THAT CONTAIN AT LEAST ONE SEARCH TERM:\n"
        for line_number in union:
            print "Line %d: %s" % (line_number, strlist[line_number])
    else:
        print "\nTHE SEARCH TERM(S) DON'T APPEAR ANYWHERE IN THE INPUT TEXT.\n"
        quit() # If no lines contained ANY term, no lines can contain EVERY term.

    intersection = sorted_search(index, query, 'AND')

    if intersection:
        print "\nLINES THAT CONTAIN EVERY SEARCH TERM:\n"
        for line_number in intersection:
            print "Line %d: %s" % (line_number, strlist[line_number])
    else:
        print "\nNO LINES CONTAINED EVERY SEARCH TERM.\n"

try_vulgar_search()
