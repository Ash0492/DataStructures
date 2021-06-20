def sumElement(n,arr):
    sum=0
    for i in range(0,n):
        sum=sum+arr[i]
        i+=1
    return sum


arr=[1,2,3,4]
n=4
print(sumElement(n,arr))