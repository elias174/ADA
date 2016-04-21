from HeapSort import heap


def heap_maximum(A):
    return A[0]


def heap_extract_max(A, size):
    if size < 0:
        return
    max = A[0]
    A[0] = A[size]
    size -= 1
    MaxHeapify(A, size, 0)
    return max


def heap_increase_key(A,i,key):
    if key < A[i]:
        return
    A[i] = key
    while i > 0 and A[Parent(i) < A[i]]:
        A[i], A[Parent(i)] = A[Parent(i)], A[i]
        i = Parent(i)


def max_heap_insert(A, size, key):
    size += 1
    A[size] = float('inf')*-1
    heap_increase_key(A, size, key)


if __name__ == '__main__':
    li = [9, 16, 4, 10, 1, 23, 12]
    li = Sort(li)
    max_heap_insert(A, len(li), 5)
    print li