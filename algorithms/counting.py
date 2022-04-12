def counting_sort(A: list, n: int):

    max_element = int(max(A))
    min_element = int(min(A))
    interval = max_element - min_element

    #Temporary array to compute frequency and cumulative sum
    C = [0 for i in range(0, interval + 1)]
    #Sorted array
    B = [0 for i in range(0, n)]

    #Store frequency of each element from array A in C
    for i in range(0,n):
        C[A[i]-min_element] += 1
    
    #Compute cumulative sum of C elements
    for i in range(1,len(C)):
        C[i] += C[i-1]
    
    i = len(A) - 1
    while i >= 0:
        B[C[A[i] - min_element] - 1] = A[i]
        C[A[i] - min_element] -= 1
        i -= 1
    for i in range(0,n):
        A[i] = B[i]
    
    return A