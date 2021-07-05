def sumOfDigits(n):
    if n<10:
        return 1
    return sumOfDigits(n//10)+n%10

n=925
print(sumOfDigits(n))