# have to ask Dr. Borie about this one
# mainly because it gives incorrect
# output

import sys
A = [10, 11, 12, 13, 14, 15, 18]
inf = sys.maxint

def two_sum(n, p, q):
    r, s, t = inf, inf, inf
    if(n < 0):
        if p == 0 and q == 0:
            return 0
        else:
            return inf
    else:
        # don't include A[n] at all
        r = two_sum(n-1, p, q)
        if A[n] <= p:
            # include A in p
            s = two_sum(n-1, p-A[n], q) + 1
        if A[n] <= q:
            # include A[n] in q
            t = two_sum(n-1, p, q-A[n]) + 1
        
        return min(r,s,t)

def two_sum2(n, p, q):
    r, s, t = inf, inf, inf
    if(n == len(A)):
        if p == 0 and q == 0:
            return 0
        else:
            return inf
    else:
        # don't include A[n] at all
        r = two_sum2(n+1, p, q)
        if A[n] <= p:
            # include A in p
            s = two_sum2(n+1, p-A[n], q) + 1
        if A[n] <= q:
            # include A[n] in q
            t = two_sum2(n+1, p, q-A[n]) + 1
        
        return min(r,s,t)



print two_sum(len(A)-1, 29, 33)
print two_sum2(0, 29, 33)
