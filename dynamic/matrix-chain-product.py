import sys
# Multiply a chain of compatible matricies
# Each matrix Mj has dimensions D[j-1] rows and D[j] columns

# Example M1M2M3 hwere D[0...3] = {10, 20, 5, 30}
# M1 is a 10x20, M2 is a 20x5, M3 is a 5x30

# (M1 M2) M3 takes 10*20*5+10*5*30 = 2500
# M1 (M2 M3) takes 20*5*30+10*20*30 = 9000

# Goal: Compute M1M2M3...Mn using fewest scalar products

# Let Cost[i][j] = fewest scalar products to compute Mi...Mj
# Find best parenthesization (Mi...Mk)(Mk+1...Mj)

# Cost[i][j] = 0 when i == j
# Cost[i][j] = min(Cost[i][k] + Cost[k+1][j] +
#               D[i-1]*D[k]*D[j] | i <= k <= j-1) when i < j

#   |0   A|
#   | 0   |
#   |  0  |
#   |   0 |
#   |    0|

def mcp(d):
    n = len(d)
    cost = [[0 for x in range(0, n)] for y in range(0, n)]
    for i in range(1, n):
        cost[i][i] = 0
    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            cost[i][j] = sys.maxint
            for k in range(i, j):
                t = cost[i][k] + cost[k+1][j] + d[i-1]*d[k]*d[j]
                if t < cost[i][j]:
                    cost[i][j] = t
    return cost

print mcp([7, 8, 5, 10, 6])

