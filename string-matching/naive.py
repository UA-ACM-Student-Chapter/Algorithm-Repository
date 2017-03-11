# Patten P[1...m]
# Text T[1...n]

def naive_string_match(text, pattern):
    for s in range(0, len(text) - len(pattern)):
        if pattern == text[s : s + len(pattern)]:
            print "pattern occurs with shift ", s

p = "aab"
text = "acaabc"

naive_string_match(text, p)

p = "abacaba"
t = "ababbabacabacababacabaa"

print "PATTERN: ", p
print "TEXT:    ", t

naive_string_match(t, p)
