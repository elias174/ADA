import math


def find_max_subarray_brute_force(A, low, high):
    left = 0
    right = 0
    sum = float('inf')*-1
    i = low
    while i <= high:
        current_sum = 0
        j = i
        while j <= high:
            current_sum += A[j]
            if current_sum > sum:
                sum = current_sum
                left = i
                right = j
            j += 1
        i += 1
    return (left, right, sum)
