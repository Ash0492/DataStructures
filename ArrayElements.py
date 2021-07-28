def printArrayRecursively(arr,n):
    if n==0:
        return
    printArrayRecursively(arr,n-1)
    print(arr[n-1],end=' ')


n=3
arr=[3,2,5]
printArrayRecursively(arr,n)