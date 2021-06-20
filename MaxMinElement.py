def maximumElement(arr,n):
    arr= sorted(arr)
    return arr.pop()

def minimumElement(arr,n):
    arr=sorted(arr)
    return arr.pop(0)

n=4
arr=[5,4,2,1]

print(maximumElement(arr,n) , minimumElement(arr,n))

