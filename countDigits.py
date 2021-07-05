def CountDigits(n):
    if n==0:
        return 0
    return 1 + CountDigits(n//10)


n=123456789
print(CountDigits(n))