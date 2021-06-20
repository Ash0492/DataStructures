def nonRepElem(arr,n):
    dict={}
    for i in arr:
        dict[i]=0

    for i in arr:
        dict[i]+=1

    l = []

    for i in arr:
        if dict[i] ==1:
            l.append(i)

    return l

arr=[1,1,2,2,3,3,4,5,6,7]
n =9
print(nonRepElem(arr,n))