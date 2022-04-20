def left(pos: int):
    return 2 * pos + 1

def right(pos: int):
    return 2 * pos + 2

def max_heapify(A: list, pos: int):
    l_child_pos = left(pos)
    r_child_pos = right(pos)

    if l_child_pos < len(A) and A[l_child_pos] > A[pos]:
        largest_pos = l_child_pos
    else:
        largest_pos = pos
    if r_child_pos < len(A) and A[r_child_pos] > A[largest_pos]:
        largest_pos = r_child_pos
    if largest_pos != pos:
        A[pos], A[largest_pos] = A[largest_pos], A[pos]
        max_heapify(A, largest_pos)
    return A

def run_max_heap(A: list, n: int):
    mid_pos = int((n//2)-1)
    while mid_pos >= 0:
        max_heapify(A,mid_pos)
        mid_pos -= 1
    return A