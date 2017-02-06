# in the format val, weight
A = [(60, 10), (100,20), (120,30)]

def knapsack(items, max_weight):
    K = [[0 for x in range(0, max_weight + 1)] \
        for y in range(0, len(items) + 1)]

    # Need to iterate to len(items) + 1 because
    # that index 1 is including item 0, not item 1.
    for i in range(0, len(items) + 1):
        # w has to iterate because you could have
        # capacity of 0
        for w in range(0, max_weight + 1):
            # however if either of them are zero,
            # our K is going to be zero.
            if i == 0 or w == 0:
                K[i][w] = 0
            # max if not including the item vs including the item
            elif items[i-1][1] <= w:
                K[i][w] = max(K[i-1][w], K[i-1][w-items[i-1][1]] +
                    items[i-1][0])
            # too much to fit. Take next best.
            else:
                K[i][w] = K[i-1][w]

    return K


print knapsack(A, 50)
