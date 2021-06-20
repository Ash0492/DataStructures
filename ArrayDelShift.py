def ArrayDelShift(arr,n,idx):
    for i in range(idx, n-1):
        arr[i] = arr[i + 1]
    arr[-1] = 0
    print(arr)


n = 5
idx = 0
arr=[1,2,3,4,5]
ArrayDelShift(arr,n,idx)
