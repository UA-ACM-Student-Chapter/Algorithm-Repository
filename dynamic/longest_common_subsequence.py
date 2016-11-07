"""
Longest Common Subsequence
Author: Jacob Zarobsky

Takes two (2) parameters and returns
the longest common subsequence between
them.

1 2 3
4 . 5
6 7 8

TODO: Fix indexing errors from Cormen
"""

def lcs_length(x, y):
    m, n = len(x), len(y)
    b = [[0 for x in range(m)] for y in range(n)]
    c = [[0 for x in range(m)] for y in range(n)]

    for i in range(0, m):
        for j in range(1, n):
            if x[i] == y[j]:
                c[i][j] = c[i - 1][j-1] + 1
                b[i][j] = 1
            elif c[i - 1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = 2
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = 4
    return [c, b]

def print_lcs(b, X, i, j):
    if i == 0 or j == 0:
        return
    if b[i][j] == 1:
        print_lcs(b, X, i - 1, j - 1)
        print(X[i])
    elif b[i][j] == 2:
        print_lcs(b, X, i- 1, j)
    else:
        print_lcs(b, X, i, j - 1)
a = "abcdefghijklmnopqrstuvwxyz"
b = "xyzabcdefghijklmnopqrstuvw"

ans = lcs_length(a,b)

print_lcs(ans[1], a, len(a) - 1, len(b) - 1)
