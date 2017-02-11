inf = float('inf')

class Vertex(object):
    
    def __init__(self, d, pi):
        self.d = inf
        self.pi = None
    
def relax(u, v, w):
    if(v.d > u.d + w(u, v)):
        v.d = u.d + w(u,v)
        v.pi = u

def init_ss(G, s):
    pass
def extend_sp(l, w):
    n = len(l)
    lp = [[float('inf') for x in range(n)] for y in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                lp[i][j] = min(lp[i][j], l[i][k] + w[k][j])
    return lp

def slow_apsp(w):
    n = len(w)
    l1 = w
    L = [ l1 ]
    for m in range(1, n):
        L.append(extend_sp(L[m-1], w))
        print L[len(L) - 1]
        raw_input()


    return L[len(L) - 1]

def faster_apsp(w):
    n = len(w)
    l1 = w
    L = [l1]
    m = 1
    while m < n - 1:
        matrix = L[len(L) - 1]
        L.append(extend_sp(matrix, matrix))
        m = 2 * m
        print L[len(L) - 1]
        raw_input()
    return L[len(L) - 1]


inf = float('inf')

w = [
    [ 0, inf, inf, inf, -1, inf],
    [ 1, 0, inf, 2, inf, inf],
    [ inf, 2, 0, inf, inf, -8],
    [-4, inf, inf, 0, 3, inf],
    [inf, 7, inf, inf, 0, inf],
    [inf, 5, 10, inf, inf, 0]
]

w2 = [
    [ 0, 5, inf, inf, 9, inf, inf, 8],
    [ inf, 0, 12, 13, inf, inf, inf, 4],
    [ inf, inf, 0, 3, inf, inf, 11, inf],
    [ inf, inf, inf, 0, inf, inf, 9, inf],
    [ inf, inf, inf, inf, 0, 4, 20, 5],
    [ inf, inf, 1, inf, inf, 0, inf, inf],
    [ inf, inf, inf, inf, inf, inf, 0, inf],
    [ inf, inf, 7, inf, inf, 6, inf, 0]
]

print "SLOWER"
print "============="
print slow_apsp(w)

print "FASTER"
print "============="
print faster_apsp(w)
print faster_apsp(w2)

