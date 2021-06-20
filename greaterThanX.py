def greaterThanX(arr,n,x):
    count = 0
    for i in arr:
        if i > x:
            count = count + 1
    print(count)