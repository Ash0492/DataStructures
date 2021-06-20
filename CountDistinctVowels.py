def countDistinctVowels(str):
    vowels = "aeiou"
    total = 0
    for i in vowels:
        if i in str:
            total=total+1
    print(total)



str="woaarld"
countDistinctVowels(str)