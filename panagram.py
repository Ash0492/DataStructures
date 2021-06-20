def Panagram(s):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in s.lower():
            return 0
    return 1

s= "Thequickbrownfoxjumpsoverthelazydog"
print(Panagram(s))
