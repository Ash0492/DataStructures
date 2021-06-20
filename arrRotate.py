def arrRotate(A,N,D):
    reverse(A,0,D-1)
    reverse(A,D,N-1)
    reverse(A,0,N-1)

def reverse(A,B,E):
    while(B<E):
        A[B], A[E] = A[E], A[B]
        B=B+1
        E=E-1

A=[10,20,30,40,50]
D=3
N=5
arrRotate(A,N,D)
print(A)