
def distinct_of_size(n):
    C = [None for x in range(n + 1)]
    C[0] = 1
    for k in range(1, n + 1):
        C[k] = 0
        for r in range(1, k + 1):
            C[k] += C[r - 1] * C[k - r]
    return C[n-1]

for i in range(1, 10):
    print distinct_of_size(i)
