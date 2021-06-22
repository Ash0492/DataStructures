from collections import Counter
def ElectionWinner(arr,n):
    for i in range(0,n):
        print(arr,arr.count(arr[i]))


arr=["john","johnny","jackie","johnny","john" "jackie","jamie","jamie","john","johnny","jamie","johnny","john"]
#arr=["andy","blake","clark"]
n =3
ElectionWinner(arr,n)
