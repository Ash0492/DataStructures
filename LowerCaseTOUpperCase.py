def caseConversion(s):
    slist=[]
    for i in range(0,len(s)):
        if s[i].islower():
            slist.append(s[i].upper())
        else:
            slist.append(s[i].lower())
    return "".join(slist)




s="FDj"
print(caseConversion(s))