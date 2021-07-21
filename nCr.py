def nCr(n,r):
    if n==0 or r==0 or n==r:
        return 1
    return nCr(n-1,r-1)+nCr(n-1,r)


n=5
r=2
print(nCr(n,r))