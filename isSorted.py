def isSorted(arr,n):
    a1 = arr[:]
    a1.sort()
    a2 = arr[::-1]
    a2.sort(reverse=True)
    if a1 == arr or a2 == arr:
        return 1
    else:
        return 0





arr=[9, 5, 25, 69, 49, 82, 69, 60, 7, 22, 23, 39, 9, 74, 56, 13, 86, 16, 90, 31, 18, 90, 68, 43, 16, 62, 20, 98, 23, 59, 46, 72, 50, 8, 91]
n=35
#arr=[1,1,2,2,3]
#n=5
print(isSorted(arr,n))
