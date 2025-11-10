"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = None
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3

def _compute_lps(pattern):
    """
    Compute LPS (longest proper prefix which is also suffix) array for KMP.
    Works for a pattern which is a list of items.
    """
    lps = [0] * len(pattern)
    length = 0  # length of previous longest prefix suffix
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def is_sublist_kmp(small, big):
    """
    Return True if 'small' is a contiguous subsequence of 'big'.
    Uses KMP matching where both pattern and text are lists.
    """
    if not small:
        # empty list is sublist of any list
        return True
    if len(small) > len(big):
        return False

    lps = _compute_lps(small)
    i = 0  # index for big (text)
    j = 0  # index for small (pattern)

    while i < len(big):
        if big[i] == small[j]:
            i += 1
            j += 1
            if j == len(small):
                return True
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False

def sublist(A, B):
    if A == B:
        return EQUAL
    if is_sublist_kmp(A, B):
        return SUBLIST
    if is_sublist_kmp(B, A):
        return SUPERLIST
    return UNEQUAL


