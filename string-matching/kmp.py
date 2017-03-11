# P[1...m]
# T[1...n]

def fail_function(p):
    m = len(p)
    fail = [0 for x in range(m)]
    fail[0] = 0
    k = 0
    for q in range(1,m):
        while k > 0 and p[k] != p[q]:
            k = fail[k-1]
        if p [k] == p[q]:
            k = k + 1
        fail[q] = k
    return fail

def kmp_match(t, p):
    n = len(t)
    m = len(p)

    fail = fail_function(p)
    
    q = 0
    print fail
    for i in range(n):
        while q > 0 and p[q] != t[i]:
            q = fail[q-1]
        if p[q] == t[i]:
            q = q + 1
        if q == m:
            print "pattern starts with shift ", i - m + 1
            q = fail[q-1]

p = "abacaba"
t = "ababbabacabacababacabaa"

kmp_match(t, p)
