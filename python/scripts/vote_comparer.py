"""Adapted from an exercise in "Coding the Matrix". This script ingests
a text file, generates a dictionary containing the voting records of diff-
erent Senators, and surfaces methods for comparing those voting records.
There is no validation or sanitization.
"""

from vec import *

def generate_voting_dict(strlist, index_of_first_vote):
    """Ingest a list of strings each of which represents one Senator's
    voting record. Return a dictionary mapping Senators to their votes. 
    Strings may contain additional information (such as State or party
    affiliation) hence the use of index_of_first_vote.
    """
    voting_records = {}

    for i in range(len(strlist)):
        record = strlist[i].split(' ')
        sen_name = record[0]
        sen_votes = [int(vote) for vote in record[index_of_first_vote:]] 

        voting_records[sen_name] = sen_votes

    return voting_records


def policy_compare(sen_a, sen_b, voting_dict):
    if sen_a in voting_dict and sen_b in voting_dict:
        return dot_prod(voting_dict[sen_a], voting_dict[sen_b])
    else:
        return 0

def most_similar(sen_a, voting_dict):
    best_match = 0
    most_similar_sen = ''
    for sen_b in voting_dict.keys():
        if sen_a == sen_b: continue # skip self
        similarity = policy_compare(sen_a, sen_b, voting_dict)
        if similarity > best_match:
            best_match = similarity
            most_similar_sen = sen_b

    percent_agreement = 100. * best_match / len(voting_dict[sen_a])
    print "\nSenator %s agreed with Senator %s %d percent of the time.\n" % (most_similar_sen, sen_a, percent_agreement)
    return
    

def least_similar(sen_a, voting_dict):
    worst_match = len(voting_dict[sen_a])
    least_similar_sen = ''
    for sen_b in voting_dict.keys():
        if sen_a == sen_b: continue # skip self
        similarity = policy_compare(sen_a, sen_b, voting_dict)
        if similarity < worst_match:
            worst_match = similarity
            least_similar_sen = sen_b
    
    percent_agreement = 100. * worst_match / len(voting_dict[sen_a])
    print "\nSenator %s and Senator %s agreed only %d percent of the time.\n" % (least_similar_sen, sen_a, percent_agreement)

    return

def list_names(dict):
    print dict.keys()

def dict_from_file():
    """Read from the data dump that accompanied this exercise."""
    text = open('../src/voting_record_dump109.txt')
    strlist = text.readlines()

    return generate_voting_dict(strlist, 3)
