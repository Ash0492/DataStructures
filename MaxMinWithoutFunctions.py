def Max(arr,n):
    max=0
    for i in range(n):
        if arr[i]>max:
            max=arr[i]
            print(max)


def Min(arr,n):
    for i in range(0,n-1):
        min=0
        if arr[i] < arr[i+1]:
            min=arr[i]
        else:
           min=arr[i+1]
        i+=1
        print(min)




n=1
arr=[1,2,21,3]
Max(arr,n)
Min(arr,n)