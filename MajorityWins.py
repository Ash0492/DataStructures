def MajorityWins(arr, n, x, y):
    countX = 0
    countY = 0
    for i in arr:
        if i==x:
            countX+=1
        if i==y:
            countY+=1
    if countX>countY:
        return x
    if countY>countX:
        return y
    if countX==countY:
        if x>y:
            return y
        else:
            return x


n=11
arr=[98,99,39,12,0,36,15,47,79,62,64]
x=64
y=5

print(MajorityWins(arr, n, x, y))



















