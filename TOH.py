moves=0
def toh(moves,N, fromm,to,aux):

    if N==1:
        print("move disk", N, "from rod", fromm, "to rod", aux)
        moves+=1
        print(moves)

    toh(moves, N-1, fromm,aux,to)
    print("Move disk", N, "from rod", fromm, "to rod", aux)
    moves+=1
    toh(moves,N-1, to,fromm,aux)
    print(moves)



N=1
toh(moves,N,'1','2','3')

