# Pattern P[1...m]
# Text T[1..n]


def build_state_table(p, alphabet):
    m = len(p)
    table = [dict((char, 0) for char in alphabet) for x in range(0,m + 1)]
    for q in range(m):
        for char in alphabet:
            k = min(m, q + 1)
            while (p[:q]+char)[-k:] != p[:k]:
                k -= 1
            table[q][char] = k if k > 0 else 0
    return table

def fsm(t, p, state_table):
    n = len(t)
    m = len(p)
    q = 0 # q is our current state
    for i in range(n):
        q = state_table[q][t[i]]
        if q == m:
            print "pattern occurs with shift ", i - m + 1
            

p = "abacaba"
t = "ababbabacabacababacabaa"
fsm(t, p, build_state_table(p, "abc"))
