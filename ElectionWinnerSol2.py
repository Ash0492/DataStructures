from collections import OrderedDict
def Winner(arr,n):
    mp = OrderedDict({})

    for i in arr:
        mp[i]= mp.get(i,0)+1

    maxx=-1
    ans=""

    mp=OrderedDict(sorted(mp.items()))

    for key,value in mp.items():
        if value>maxx:
            maxx=value
            answer=key
    result=[answer,maxx]
    print(result)



arr=["john","johnny","jackie","johnny","john","jackie","jamie","jamie","john","johnny","jamie","johnny","john"]
#arr=["andy","blake","clark"]
n =13
Winner(arr,n)