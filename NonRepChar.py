class solution:
    def nonrepeatingcharacter(self,s):
        occurrences=[0 for i in range(256)]
        for char in s:
            occurrences[ord(char)]+=1

        for i in range(len(s)):
            if(occurrences[ord(s[i])])==1:
                return s[i]
        return '$'



s="aabcdebbbghi"
char = solution()
print(char.nonrepeatingcharacter(s))
