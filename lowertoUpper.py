def LowertoUpper(s):
    slist=[]
    for i in s:
        if i.islower():
            slist.append(i.upper())
        else:
            slist.append(i)
    return "".join(slist)


s = "FDj"
print(LowertoUpper(s))