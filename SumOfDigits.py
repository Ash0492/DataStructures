def SumOfDigits(n):
    if n<10:
        return n
    return SumOfDigits(n//10)+n%10


n=253
print(SumOfDigits(n))