from typing import List

def counting_for_radix(A: list, exp: int, n: int):

    
    #Output sorted array
    output = [0] * (n)
    #Temporary array to compute frequency and cumulative sum
    count = [0] * (10)

    #counting array to compute frequency of elements between 0 and 9
    for i in range(0, n):
        index = A[i] // exp
        count[index % 10] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = A[i]//exp
        output[count[index  % 10]-1] = A[i]
        count[index  % 10] -= 1
        i -= 1

    i = 0
    for i in range(0,n):
        A[i] = output[i]
    return A


def radix(A: list, n: int):
    max_el = max(A)
    pos = []
    neg = []
    for a in A:
        if a >= 0:
            pos.append(a)
        else:
            neg.append(a)

    dig = 1
    while max_el/dig > 1:
        neg = counting_for_radix(neg,dig,len(neg))
        pos = counting_for_radix(pos,dig,len(pos))
        dig *= 10
    
    return neg+pos