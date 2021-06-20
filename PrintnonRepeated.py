from collections import Counter
def printNonRepeat(arr,n):
    return [i for i in arr if arr.count(i)<2]


l = [1, 1, 2, 2, 3, 3, 8, 5, 6, 7]

print(printNonRepeat(l, len(l)))