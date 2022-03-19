def selection_sort(A: list, n:int):
    for i in range(0, n):
        min = i
        for j in range(i+1, n):
            if A[j] < A[min]:
                min = j
        (A[i],A[min]) = (A[min],A[i])
    return A