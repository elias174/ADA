import math


def merge(A, p, q, r):
    L = [A[i] for i in range(p, q+1)]
    R = [A[i] for i in range(q+1, r+1)]

    L.append(float('inf'))
    R.append(float('inf'))

    print L, R
    i = 0
    j = 0
    k = p
    while k <= r:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1


def mergesort(A, p, r):
    if p < r:
        q = (p+r)/2
        mergesort(A, p, q)
        mergesort(A, q+1, r)
        merge(A, p, q, r)

d = [4, 6, 7, 8, 1, 3, 5, 7]
#d = [3, 1, 3, 4, 2, 1, 2421412, 2, 15125125, 122, 0]
mergesort(d,0,len(d)-1)
print d