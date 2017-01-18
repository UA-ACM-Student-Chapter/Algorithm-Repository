# start at the endpoint and
# work your way out

def find_max_crossing_subarray(a, low, mid, high):
    print a, low, mid, high
    left_sum = float("-inf")
    result_sum = 0
    max_left = mid
    max_right = mid + 1
    for i in range(mid, low, -1):
        result_sum = result_sum + a[i]
        if result_sum > left_sum:
            left_sum = result_sum
            max_left = i
    right_sum = float("-inf")
    for j in range(mid + 1, high):
        result_sum = result_sum + a[j]
        if result_sum > right_sum:
            right_sum = result_sum
            max_right = j
    return (max_left, max_right, left_sum + right_sum)

def find_max_subarray(a, low, high):
    if high == low:
        return (low, high, a[low])
    else:
        mid = (low + high) / 2
        left_low, left_high, left_sum = find_max_subarray(a, low, mid)
        right_low, right_high, right_sum = find_max_subarray(a, mid+1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(a, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)
print find_max_subarray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7], 0, 15)

