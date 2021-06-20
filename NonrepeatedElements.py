from collections import Counter
def cDistinct(l):
    count=0
    res = Counter(l)
    for i in res:
        if res[i] ==1:
            count=count+1
    return count



l = [1,1,2,2,3,3,8,5,6,7]

print(cDistinct(l))