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

def sortedSearch(index, query, operator = 'OR'):
  values = search(index, query, operator)
  values = [x for x in values]
  values.sort()

  return values
