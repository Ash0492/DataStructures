import re

def validate(s):
    if len(s) < 10:
        return 0
    p = re.compile('^(?=.*[!$#?\-*@])(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])')

    if re.search(p, s):
        return 1
    else:
        return 0




s= "FTfQHlbUh#roSrhCQ"
print(validate(s))
