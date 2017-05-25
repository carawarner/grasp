# Adapted from an exercise in "Coding the Matrix"

from string import punctuation

# Given a list of strings representing lines of text, returns the set
# that maps each word of each line to the line number(s) on which it
# appears. 
def makeInverseIndex(strlist):
  index = {}

  for i in range(1, len(strlist)):
    line = sanitize(strlist[i])
    words = line.split(' ')

    for word in words:
      if word == '': continue
      if word in index:
        index[word].add(i)
      else:
        index[word] = {i}

  return index


# Strips punctuation and standardizes case to maximize search results.
def sanitize(s):
  return s.translate(None, punctuation + '\n').lower()


# Given an index and a query (a list of words), returns the set of all
# line numbers for lines that contain ANY/ALL of the words, as decided
# by the operator (OR,AND).
def search(index, query, operator = 'OR'):
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

# Takes the set of values returned by search(), converts it to a list
# and sorts that list. Uses default sort.
def sortedSearch(index, query, operator = 'OR'):
  values = search(index, query, operator)
  values = [x for x in values]
  values.sort()

  return values

# Provides a way to interact with vulgar_search fro the CL
def try_vulgar_search():
  print "\n"

  query = []  

  while(True):
    term = str(raw_input("Add a search term (if you're done just hit enter): "))
    if term == '':
      break
    
    query.append(term)

  f = open('src/leaves.txt')
  strlist = f.readlines()
  index = makeInverseIndex(strlist)

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
  

try_vulgar_search()
