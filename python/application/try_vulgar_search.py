from scripts.vulgar_search import makeInverseIndex, sortedSearch

# Prompts the user to enter search terms. Inlcudes no validation whatsoever.
def solicitSearchTerms():
  q = []

  while(True):
    term = str(raw_input("Add a search term (if you're done just hit enter): "))
    if term == '':
      break

    q.append(term)

  return q 

# Setup
f = open('data/leaves.txt')
strlist = f.readlines()
index = makeInverseIndex(strlist)
query = solicitSearchTerms()

# Search

union = sortedSearch(index, query, 'OR')

if len(union) > 0:
  print "\nLINES THAT CONTAIN AT LEAST ONE SEARCH TERM:\n"
  for line_number in union:
    print "Line %d: %s" % (line_number, strlist[line_number])
else:
  print "\nTHE SEARCH TERM(S) DON'T APPEAR ANYWHERE IN THE INPUT TEXT.\n"
  quit() # If no lines contained ANY term, no lines can contain EVERY term.

intersection = sortedSearch(index, query, 'AND')

if len(intersection) > 0:
  print "\nLINES THAT CONTAIN EVERY SEARCH TERM:\n"
  for line_number in intersection:
    print "Line %d: %s" % (line_number, strlist[line_number])
else:
  print "\nNO LINES CONTAINED EVERY SEARCH TERM.\n"

