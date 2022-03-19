def insertion_sort(A: list, n:int):
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j]>key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
        if i == round(n/4):
            print('----25% concluded----')
        elif i == round(n/2):
            print('----50% concluded----')
        elif i == round(3*n/4):
            print('----75% concluded----')
    return A