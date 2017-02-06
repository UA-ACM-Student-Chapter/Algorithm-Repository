# start at the mid point and
# work your way out

# | ---- <- mid -> ----|

def find_max_crossing_subarray(a, low, mid, high):
    left_sum = float("-inf") # initalize so it will be replaced.
    result_sum = 0 # set current sum to zero
    max_left = mid # set our max left to our start point
    max_right = mid + 1 # set our max right to our start point + 1
    for i in range(mid, low, -1): # count down to low
        result_sum = result_sum + a[i] # keep a running sum
        if result_sum > left_sum:
            left_sum = result_sum   # replace our max if necessary
            max_left = i    # and then update our max i
    right_sum = float("-inf") # start this, but go oposite direction
    for j in range(mid + 1, high):
        result_sum = result_sum + a[j]
        if result_sum > right_sum:
            right_sum = result_sum
            max_right = j
    return (max_left, max_right, left_sum + right_sum)

def find_max_subarray(a, low, high):
    # base case
    if high == low: return (low, high, a[low])
    mid = (low + high) / 2
    # must be strictly in our left
    left_low, left_high, left_sum = find_max_subarray(a, low, mid)
    # or strictly in our right
    right_low, right_high, right_sum = find_max_subarray(a, mid+1, high)
    # or cross the mid point
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(a, low, mid, high)
    if left_sum >= right_sum and left_sum >= cross_sum:
        return (left_low, left_high, left_sum)
    if right_sum >= left_sum and right_sum >= cross_sum:
        return (right_low, right_high, right_sum)
    return (cross_low, cross_high, cross_sum)

print find_max_subarray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7], 0, 15)

