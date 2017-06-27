# pylint: disable=consider-using-enumerate
"""Helper functions for dealing with vectors."""


def add_vecs(vectors):
    """Add 2 or more vectors. Return a vector."""
    if len(vectors) <= 1:
        return

    if len(vectors) == 2:
        vec_a = vectors[0]
        vec_b = vectors[1]
        return [vec_a[i] + vec_b[i] for i in range(len(vec_a))]

    #Add first element to the sum of remaining elements
    return add_vecs([vectors[0], add_vecs(vectors[1:])])


def average_vecs(vectors):
    """Divide the sum of all vectors by the number of vectors.
    Return a vector.
    """
    summed = add_vecs(vectors)
    num_elements = float(len(vectors))
    return [elem / num_elements for elem in summed]


def dot_prod(vec_a, vec_b):
    """Calculate the dot product of two vectors."""
    return sum_vec(multiply_vecs([vec_a, vec_b]))


def multiply_vecs(vectors):
    """Multiply 2 or more vectors. Return a vector."""
    if len(vectors) <= 1:
        return

    if len(vectors) == 2:
        vec_a = vectors[0]
        vec_b = vectors[1]
        return [vec_a[i] * vec_b[i] for i in range(len(vec_a))]

    #Multiply first element by the product of remaining elements
    return multiply_vecs([vectors[0], multiply_vecs(vectors[1:])])


def scale_vec(vector, scalar):
    """Multiple each element in a vector by some scalar. Return a vector."""
    return [vector[i] * scalar for i in range(len(vector))]


def sum_vec(vector):
    """Combine the elements of a single vector. Return a number or string."""
    vec_sum = 0
    for i in range(len(vector)):
        vec_sum += vector[i]

    return vec_sum


def translate_vec(vector, addend):
    """Add some number to each element in a vector. Return a vector."""
    return [vector[i] + addend for i in range(len(vector))]
