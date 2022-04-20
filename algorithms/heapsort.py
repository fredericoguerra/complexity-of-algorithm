def heapify(A: list, n: int, i: int):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and A[i] < A[l]:
        largest = l

    if r < n and A[largest] < A[r]:
        largest = r

    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        heapify(A, n, largest)

def heap_sort(A: list, n: int):

    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)

    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)