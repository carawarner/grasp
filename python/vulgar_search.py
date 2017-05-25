# Adapted from an exercise in "Coding the Matrix"

from string import punctuation

# Given a list of strings representing lines of text, returns the set
# that maps each word of each line to the line number(s) on which it
# appears. 
def makeInverseIndex(strlist):
  
  # for each line
  # add each word to a set
  # if word already a key in set, update its value
  # if word not yet a key in set, add it
  # for now, don't worry about punctuation and case
  # also don't worry about tracking words appearing > 1 on a line

  index = {}

  for i in range(1, len(strlist)):
    string = sanitize(strlist[i])
    words = string.split(' ')

    for word in words:
      if word == '': continue
      if word in index:
        index[word].append(i)
      else:
        index[word] = [i]

  return index

def sanitize(s):
  return s.translate(None, punctuation + '\n').lower()

# Given an inverse index and a query (a list of words), returns the set
# containing line numbers for lines that contain ANY of the query words.
def orSearch(inverseIndex, query):
  return ""

# Given an inverse index and a query (a list of words), returns the set
# containing line numbers for lines that contain ALL of the query words.
def andSearch(inverseIndex, query):
  return ""

# Testing
f = open('data/leaves.txt')
strlist = f.readlines()
inverse_index = makeInverseIndex(strlist)
