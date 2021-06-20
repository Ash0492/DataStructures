def immediateSmaller(arr,n,x):
    ans = -1
    diff = 10000000
    for e in arr:
        if e > x and e-x < diff:
            ans = e
            diff = e-x
    return ans



arr = [1,2,3,4,5]
n = 5
x = 1
print(immediateSmaller(arr, n, x))


