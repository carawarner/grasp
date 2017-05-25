# pylint: disable=no-else-return
"""Adapted from an exercise in "Coding the Matrix"
"""

from string import punctuation

def make_inverse_index(strlist):
    """Given a list of strings representing lines of text, builds a set
    which maps each word of each line to the line number(s) on which it
    appears
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
    """Strips punctuation and line endings. Standardizes case to make
    search case-insensitive
    """
    return str_to_sanitize.translate(None, punctuation + '\n').lower()


def search(index, query, operator='OR'):
    """Given an index and a query (a list of words), returns the set of
    all line numbers for lines that contain ANY or ALL of the words
    depending on the operator passed in.
    """
    values = []
    sanitized = []
    for term in query:
        sanitized.append(sanitize(term))

    for searchterm in sanitized:
        if searchterm in index:
            values.append(index[searchterm])

    if len(values) < 1:
        return []
    elif len(values) == 1:
        return values[0]

    if operator.upper() == 'AND':
        return values[0].intersection(*values[1:])
    else:
        return values[0].union(*values[1:])


def sorted_search(index, query, operator='OR'):
    """Converts set of values produced by search() into a list and returns
    that list sorted
    """
    values = search(index, query, operator)
    values = [x for x in values]
    values.sort()    

    return values

# Provides a way to interact with vulgar_search fro the CL
def try_vulgar_search():
    """Provides a way to interact with vulgar_search from the CL"""
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
