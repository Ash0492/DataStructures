def RecursiveSum(n):
    if n==0:
        return 0
    return RecursiveSum(n-1)+n

n=5
print(RecursiveSum(n))