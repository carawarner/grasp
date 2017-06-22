"""Helper functions for dealing with vectors."""

def sum(vec):
    sum = 0
    for i in range(len(vec)):
        sum += vec[i]

    return sum

def prod(vec_a, vec_b):
    return [vec_a[i] * vec_b[i] for i in range(len(vec_a))]

def dot_prod(vec_a, vec_b):
    return sum(prod(vec_a, vec_b))
