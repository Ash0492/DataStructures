def pm(start,end):
    print(start, '->' , end)

def TOH(n,start,end):
    if n==1:
        pm(start,end)
    else:
        other = 6-(start+end)
        h(n-1, start, other)
        pm(start,end)


