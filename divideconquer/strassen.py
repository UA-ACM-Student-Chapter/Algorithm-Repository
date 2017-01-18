def array_init(rows, cols, init=0):
    return [[init for x in range(0, cols)] for y in range(0, rows)]

# O(n^2)
def add(A, B):
    c = array_init(len(A), len(A[0]))
    for i in range(0, len(A)):
        for j in range(0, len(A[i])):
            c[i][j] = A[i][j] + B[i][j]
    return c

# O(n^2)
def scalar_mult(A, s):
    l = list(A) # gets a new list
    for i in range(0, len(l)):
        for j in range(0, len(l[0])):
            l[i][j] = l[i][j] * s
    return l

# O(n^2)
def subtract(A, B):
    return add(A, scalar_mult(B, -1))

def slice(mat, start_row, end_row, start_col, end_col):
    return [row[start_col:end_col] for row in mat[start_row:end_row]]

def strassen(A, B):
    length = len(A) / 2

    

print scalar_mult(array_init(5,5,1), 5)
