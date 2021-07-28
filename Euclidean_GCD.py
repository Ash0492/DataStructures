def gcd(a,b):

    if b==0:
        return a
    return gcd(b,a%b)

a=7
b=8
print(gcd(a,b))