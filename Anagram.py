def Anagram(a,b):
    if len(a)!=len(b):
        return "No"


    count= [0]*256

    for i in range(len(a)):
        count[ord(a[i])]+=1
        count[ord(b[i])]-= 1

    for x in count:
        if x!=0:
            return "No"
    return "Yes"



a = "b"
b= "d"
print(Anagram(a,b))