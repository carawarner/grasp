# pylint: disable=relative-import
"""Adapted from an exercise in "Coding the Matrix". This script ingests
a text file, generates a dictionary containing the voting records of diff-
erent Senators, and surfaces methods for comparing those voting records.
There is no validation.
"""

from vec import dot_prod

def generate_voting_dict(strlist, index_of_first_vote):
    """Ingest a list of strings containing Senators' names and voting
    records. Return a dictionary of the same.
    """
    records = [strlist[i].split(' ') for i in range(len(strlist))]
    voting_dict = {}

    for record in records:
        name = record[0]
        votes = [int(vote) for vote in record[index_of_first_vote:]]
        voting_dict[name] = votes

    return voting_dict


def policy_compare(sen_a, sen_b, voting_dict):
    """Return an integer that is the difference between the number of
    times the Senators agreed and the number of times they disagreed.
    If either Senator abstained from a vote, it's skipped.
    """
    if not sen_a in voting_dict or not sen_b in voting_dict:
        print "Voting record(s) unavailable for one or both Senators."
        return

    return dot_prod(voting_dict[sen_a], voting_dict[sen_b])


def most_similar(sen_a, voting_dict):
    """Identify the Senator whose voting record most closely resembles
    that of the input Senator.
    """
    most_similar_sen = None
    highest_score = -1 * len(voting_dict[sen_a]) #start with disagreeing on every vote

    senators = voting_dict.keys()
    senators.remove(sen_a)

    for sen_b in senators:
        score = policy_compare(sen_a, sen_b, voting_dict)
        if score > highest_score:
            highest_score = score
            most_similar_sen = sen_b

    print "\nThe closest match to Senator %s is Senator %s with match score %d \n" \
        % (sen_a, most_similar_sen, highest_score)
    return


def least_similar(sen_a, voting_dict):
    """Identify the Senator whose voting record is least like that of
    the input Senator.
    """
    least_similar_sen = None
    lowest_score = len(voting_dict[sen_a]) #start with agreeing on every vote

    senators = voting_dict.keys()
    senators.remove(sen_a)

    for sen_b in senators:
        score = policy_compare(sen_a, sen_b, voting_dict)
        if score < lowest_score:
            lowest_score = score
            least_similar_sen = sen_b

    print "\nThe furthest match from Senator %s was Senator %s with match score %d \n" \
        % (sen_a, least_similar_sen, lowest_score)
    return


def list_names(voting_dict):
    """Print a list of Senators' names."""
    print voting_dict.keys()


def dict_from_file():
    """Read from the data dump that accompanied this exercise."""
    text = open('../src/voting_record_dump109.txt')
    strlist = text.readlines()

    return generate_voting_dict(strlist, 3)
