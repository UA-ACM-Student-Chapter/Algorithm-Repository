"""
Greedy Activity Selector
Written by: Jake Zarobsky

Variables:
    A : Activities, sorted monotonically increasing order
        of finishing time. Each activity is is a [] of 
        [s, f] where s is the start and f is the finish.
"""

def iter_activity_selector(activities):
    activities.sort(key=lambda x: x[1]) # sort inc finish
    n = len(activities)
    results = [activities[0]]
    k = 1
    for m in range(2, n):
        if activities[m][0] >= activities[k][1]:
            results.append(activities[m])
            k = m
    return results

def test():
    activities = [[1, 4], [3, 5], [0, 6], 
        [5, 7], [3,9], [5, 9], [6, 10], [8, 11],
        [8, 12], [2, 14], [12, 16]]
    print(iter_activity_selector(activities))
test()
