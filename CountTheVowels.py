def CountTheVowels(str):
    vowels = "aeiou"
    total = 0
    for i in str:
        for j in vowels:
            if i==j:
                total = total+1
    return total



str="world"
print(CountTheVowels(str))