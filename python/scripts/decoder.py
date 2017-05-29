"""Solve a challenge posed in Coding the Matrix: "An 11-symbol message has been encrypted
as follows: Each symbol is represented by a number between 0 and 26 [... and e]ach number
is represented by a five-bit binary sequence [...]. Finally the resulting sequence of 55
bits is encrypted using a flawed version of a one-time pad: the key is not 55 random bits
but 11 copies of the same sequence of 5 random bits. Try to find the plaintext."""

def translate(binary_number, dictionary):
    """Return the symbol associated with the given binary_number. If it does not appear
    in the dictionary, return an empty string.
    """
    return dictionary[binary_number] if binary_number in dictionary else ''

def decode(cyphertext):
    """Use brute force method to decode cyphertext: loop over all possible 5 bit keys."""
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    binary_values = range(0b00000, 0b11011)
    dictionary = dict(zip(binary_values, symbols))

    for i in range(0b00000, 0b11111):
        translated = []
        for symbol in cyphertext:
            decoded = symbol ^ i
            translated.append(translate(decoded, dictionary))
        print ''.join(translated)

CYPHERTEXT = [0b10101, 0b00100, 0b10101, 0b01011, 0b11001,
              0b00011, 0b01011, 0b10101, 0b00100, 0b11001, 0b11010]

decode(CYPHERTEXT)
