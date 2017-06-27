# pylint: disable=relative-import,multiple-statements
"""Adapted from an exercise in "Coding the Matrix". This script ingests
a text file, generates a dictionary containing the voting records of diff-
erent senators, and surfaces methods for comparing those voting records.
There is limited validation.
"""

from vec import dot_prod, average_vecs

def generate_voting_dict(strlist, index_of_first_vote):
    """Ingest a list of strings containing senators' names and voting
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
    times the senators agreed and the number of times they disagreed.
    If either senator abstained from a vote, it's skipped.
    """
    if not sen_a in voting_dict or not sen_b in voting_dict:
        print "Voting record(s) unavailable for one or both senators."
        return

    return dot_prod(voting_dict[sen_a], voting_dict[sen_b])


def most_similar(sen_a, voting_dict):
    """Identify the senator whose voting record most closely resembles
    that of the input senator.
    """
    most_similar_sen = None
    highest_score = -1 * len(voting_dict[sen_a]) #start with disagreeing on every vote

    sens_b = [sen for sen in voting_dict.keys() if not sen == sen_a]

    for sen_b in sens_b:
        score = policy_compare(sen_a, sen_b, voting_dict)
        if score > highest_score:
            highest_score = score
            most_similar_sen = sen_b

    print "The closest match to Senator %s is Senator %s with match score %d \n" \
        % (sen_a, most_similar_sen, highest_score)
    return


def least_similar(sen_a, voting_dict):
    """Identify the senator whose voting record is least like that of
    the input senator.
    """
    least_similar_sen = None
    lowest_score = len(voting_dict[sen_a]) #start with agreeing on every vote

    sens_b = [sen for sen in voting_dict.keys() if not sen == sen_a]
    for sen_b in sens_b:
        score = policy_compare(sen_a, sen_b, voting_dict)
        if score < lowest_score:
            lowest_score = score
            least_similar_sen = sen_b

    print "The furthest match from Senator %s was Senator %s with match score %d \n" \
        % (sen_a, least_similar_sen, lowest_score)
    return


def find_average_similarity(sen_a, sen_set, voting_dict):
    """Compare sen_a's voting record against those of all senators in
    sen_set and return his/her agreement with the average.
    """
    sum_of_all_scores = 0.

    sens_b = [sen for sen in sen_set if not sen == sen_a]
    for sen_b in sens_b:
        sum_of_all_scores += policy_compare(sen_a, sen_b, voting_dict)

    return sum_of_all_scores/len(sens_b)


def find_average_similarity2(sen_a, sen_set, voting_dict):
    """Same as find_average_similarity() only instead of taking the average
    of the dot products, it takes the dot product of the average.
    """
    votes = [voting_dict[sen] for sen in sen_set if not sen == sen_a]
    average = average_vecs(votes)

    return dot_prod(voting_dict[sen_a], average)


def most_average(sen_set, voting_dict):
    """Finds the senator whose voting record is closest to the average
    of the records of all the sens in sen_set.
    """
    highest_score = 0
    most_average_sen = None

    for sen in sen_set:
        score = find_average_similarity2(sen, sen_set, voting_dict)
        print "%s vs the party: %d" % (sen, score)
        if score > highest_score:
            highest_score = score
            most_average_sen = sen

    return most_average_sen


def most_average2(sen_set, voting_dict):
    """Similar to most_average() but more efficient because it calculates
    a single voting average and compares senators' records agains that.
    Efficiency comes at a cost: this is less accurage for outliers."""
    highest_score = 0
    most_average_sen = None

    votes = [voting_dict[sen] for sen in sen_set]
    average = average_vecs(votes)

    for sen in sen_set:
        score = dot_prod(voting_dict[sen], average)
        if score > highest_score:
            highest_score = score
            most_average_sen = sen

    return most_average_sen


def extract_party_members(party):
    """Read from the data dump that accompanied this exercise. Return a list of
    senators who are members of the specified political party.
    """
    text = open('../src/voting_record_dump109.txt')
    strlist = text.readlines()
    records = [strlist[i].split(' ') for i in range(len(strlist))]
    sens = [records[i][0] for i in range(len(records)) if records[i][1] == party]

    return sens


def dict_from_file():
    """Read from the data dump that accompanied this exercise."""
    text = open('../src/voting_record_dump109.txt')
    strlist = text.readlines()

    return generate_voting_dict(strlist, 3)
