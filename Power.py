revr_num = 0
def reverse(N):
    global revr_num
    if(N>0):
        rem=N%10
        revr_num = (revr_num * 10) + rem
        reverse(N//10)
    return revr_num

def power(N):
    return pow(N,revr_num)%(10**9+7)

N=12
print(reverse(N))
print(power(N))


