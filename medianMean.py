def mean(A,N):
    sum=0
    for i in range(0,N):
         sum=sum+A[i]
         i+=1
    return sum//N


def median(A,N):
    A.sort()
    if N%2==0:
        mid=N//2
        mid1=A[mid]
        mid2=A[mid-1]
        median= ((mid1+mid2)//2)
        return median
    elif N%2!=0:
        l=N//2
        mid=A[l]
        return mid



A=[2,8,3,4]
N=4
print(mean(A,N), median(A,N))
