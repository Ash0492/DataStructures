def RecursivePower(n,p):
    if p==0:
        return 1
    return n* RecursivePower(n,p-1)

n=2
p=9
print(RecursivePower(n,p))
