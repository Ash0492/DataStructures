def smallerThanX(arr,n,x):
    count=0
    for i in arr:
        if i<x:
            count=count+1
    print(count)


n=6
arr = [2,2,2,2,2]
x=3

smallerThanX(arr,n,x)

