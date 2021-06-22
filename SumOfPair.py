def SumOfPAir(arr,n,sum):
    s=set()
    for i in range(0,n):
        temp=sum-arr[i]
        if temp in s:
            return 1
        s.add(arr[i])
        return s
    return 0


arr=[1,2,3,4,5,6,7,8,9,10]
n=10
sum=14
print(SumOfPAir(arr,n,sum))
