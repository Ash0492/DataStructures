def isPalin(n,rev=0):

    if n==0:
        return rev

    rev =rev*10+(n%10)
    rev= reverse(n//10,rev)
    return rev

def isPalin(num):
    if num==reverse(num):
        return 1
    else:
        return 0


n=101
print(reverse(n))
print(isPalin(n))