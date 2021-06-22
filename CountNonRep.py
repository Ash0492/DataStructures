def CountNonRepElem(arr,n):
    dict={}
    for i in arr:
        dict[i]=0

    for i in arr:
        dict[i]+=1
    counter=0

    for i in arr:
        if dict[i]==1:
            counter+=1
    return counter
arr=[10,20,30,40,10]
n=9
print(CountNonRepElem(arr,n))