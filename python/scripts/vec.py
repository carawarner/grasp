# pylint: disable=unused-variable
"""Helper functions for dealing with vectors."""

def vec_sum(vec_a, vec_b):
    """Add the elements of two vectors. Return a vector."""
    return [vec_a[i] + vec_b[i] for i in range(len(vec_a))]


def vec_sum_recursive(vectors):
    """Add the elements of more than two vectors."""
    if len(vectors) == 2:
        return vec_sum(vectors[0], vectors[1])
    return vec_sum(vectors[0], vec_sum_recursive(vectors[1:]))


def vec_sum_elements(vec):
    """Add the elements of a single vector. Return a number."""
    vsum = 0
    for i, item in enumerate(vec):
        vsum += item
    return vsum


def vec_prod(vec_a, vec_b):
    """Multiple the elements of two vectors."""
    return [vec_a[i] * vec_b[i] for i in range(len(vec_a))]


def vec_average(vectors):
    """Divide the sum of all vectors by the number of vectors."""
    summed = vec_sum_recursive(vectors)
    num_elements = float(len(vectors))
    return [elem / num_elements for elem in summed]


def dot_prod(vec_a, vec_b):
    """Calculate the dot product of two vectors."""
    return vec_sum_elements(vec_prod(vec_a, vec_b))
