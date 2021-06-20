def test(arr,n,x,y):
        for i in arr:
            countX = 0
            countY = 0
            if i==x:
                countX+=1
            if i==y:
                countY+=1
            if countX>countY:
                print(x)
            if countY>countX:
                print(y)
            elif x<y:
                print(x)

























n = 11
arr = [98, 99, 39, 12, 0, 36, 15, 47, 79, 62, 64]
x = 64
y = 5
test(arr, n, x, y)