from collections import Counter
def ElectionWinner(arr,n):
    temp=Counter(arr)
    dict={}
    for value in temp.values():
        dict[value]=[]


    for (key,value) in temp.items():
        dict[value].append(key)


    maxVote=sorted(dict.keys(),reverse=True)[0]


    if(len(dict[maxVote])>1):
        print(sorted(dict[maxVote])[0],maxVote)
    else:
        print(dict[maxVote][0], maxVote)



arr=["john","johnny","jackie","johnny","john","jackie","jamie","jamie","john","johnny","jamie","johnny","john"]
#arr=["andy","blake","clark"]
n =13
ElectionWinner(arr,n)
