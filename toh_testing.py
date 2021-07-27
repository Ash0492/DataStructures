count = 0
def Hanoi(count , N , fromm, to,aux):
    if(N == 1):
        print("move disk", N, "from rod", fromm, "to rod", aux)
        count+=1
        return count
    count = Hanoi(count , N-1, fromm, to, aux)
    print("move disk", N, "from rod", fromm, "to rod", aux)
    count+=1
    count = Hanoi(count , N-1, to, aux, fromm)
    print(count)

Hanoi(count , 3, 'A', 'C', 'B')



