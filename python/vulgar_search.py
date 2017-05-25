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

# Given an inverse index and a query (a list of words), returns the set
# containing line numbers for lines that contain ANY of the query words.
def orSearch(index, query):
  values = []

  for searchterm in query:
    if searchterm in index:
      values.append(index[searchterm])

  if len(values) <= 1:
    return values
  else:
    return values[0].union(*values[1:])

# Given an inverse index and a query (a list of words), returns the set
# containing line numbers for lines that contain ALL of the query words.
def andSearch(index, query):
  values = []

  for searchterm in query:
    if searchterm in index:
      values.append(index[searchterm])

  if len(values) <= 1:
    return values
  else:
    return values[0].intersection(*values[1:])

# Testing
f = open('data/leaves.txt')
strlist = f.readlines()
index = makeInverseIndex(strlist)
query = ['green','leaves']
print orSearch(index, query)
