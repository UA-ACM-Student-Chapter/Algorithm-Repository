import string

def alphabet(letters):
    # Get the 26 letters of the alphabet
    alpha = string.ascii_lowercase

    alpha_len = len(alpha)
    letters_len = len(letters)

    cache = {}

    for i in range(alpha_len + 1):
        cache[i, 0] = 0
    for j in range(letters_len + 1):
        cache[0, j] = 0

    for i in range(1, alpha_len + 1):
        for j in range(1, letters_len + 1):
            if alpha[i - 1] == letters[j - 1]:
                # We found matching characters in a sequence. Add 1 to the count and check the remaining letters
                cache[i, j] = 1 + cache[i - 1, j - 1]
            else:
                # The letters don't match, so try removing a letter from sequence 1 and also try removing a letter from sequence 2
                # See if that yields matching characters, and return the largest result of the two options
                cache[i, j] = max(cache[i, j - 1], cache[i - 1, j])

    result = []
    while i > 0 and j > 0:
        if alpha[i - 1] == letters[j - 1]:
            result.append(alpha[i - 1])
            i -= 1
            j -= 1
        elif cache[i - 1, j] > cache[i, j - 1]:
            i -= 1
        else:
            j -= 1

    result.reverse()
    return ''.join(result)

print(alphabet("xyzabcdefghijklmnopqrstuvw"))
