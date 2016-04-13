import math
from brute_force_sub_array import find_max_subarray_brute_force


def find_max_crossing_subarray(A, low, mid, high):
    left_sum = float('inf')*-1
    max_left = None
    sum = 0
    i = mid
    while i >= low:
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
        i -= 1
    right_sum = float('inf')*-1
    sum = 0
    j = mid + 1
    while j <= high:
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
        j += 1
    return (max_left, max_right, left_sum+right_sum)


def find_maximum_subarray(A, low, high):
    if high == low:
        return (low, high, A[low])
    else:
        mid = (low+high)/2
        (left_low, left_high, left_sum) = find_maximum_subarray(A, low, mid)
        (right_low, right_high, right_sum) = find_maximum_subarray(A, mid+1,
                                                                   high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(A, low,
                                                                        mid,
                                                                        high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)


crossover_point = 5


def mixed_find_subarray(A, low, high):
    if high-low < crossover_point:
        return find_max_subarray_brute_force(A, low, high)
    else:
        mid = (low+high)/2
        (left_low, left_high, left_sum) = find_maximum_subarray(A, low, mid)
        (right_low, right_high, right_sum) = find_maximum_subarray(A, mid+1,
                                                                   high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(A, low,
                                                                        mid,
                                                                        high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)

A = [-3, -4, 1]
maximum_index = find_maximum_subarray(A, 0, len(A)-1)
print A[maximum_index[0]:maximum_index[1]+1]
print maximum_index[2]
