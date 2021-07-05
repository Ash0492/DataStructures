def printNos(N):
     if N==0:
         return 0
     return printNos(N-1)+N



N=0
print(printNos(N))


