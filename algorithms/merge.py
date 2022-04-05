def merge_sort(A: list, n: int):
    if n > 1:
        mid_A = n//2

        left_A = A[:mid_A]
        right_A = A[mid_A:]

        merge_sort(left_A, len(left_A))
        merge_sort(right_A, len(right_A))

        i = j = k = 0

        while i < len(left_A) and j < len(right_A):
            if left_A[i] < right_A[j]:
                A[k] = left_A[i]
                i += 1
            else:
                A[k] = right_A[j]
                j += 1
            k += 1
        while i < len(left_A):
            A[k] = left_A[i]
            i += 1
            k += 1
        while j < len(right_A):
            A[k] = right_A[j]
            j += 1
            k += 1
    return A