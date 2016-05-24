import math
import time


def time_usage(func):
    def wrapper(*args, **kwargs):
        beg_ts = time.time()
        func(*args, **kwargs)
        end_ts = time.time()
        print "Time for:", func.__name__
        print("elapsed time: %f" % (end_ts - beg_ts))
    return wrapper


@time_usage
def calling_recursive_cut_rod(p, n):
    recursive_cut_rod(p, n)


def recursive_cut_rod(p, n):
    if n == 0:
        return 0
    q = float('inf')*-1
    for i in range(1, n):
        q = max(q, p[i]+recursive_cut_rod(p,n-i-1))
    return q


@time_usage
def bottom_up_cut_rod(price, n):
    val = [0 for x in range(n+1)]
    val[0] = 0
    for i in range(1, n+1):
        max_val = float('inf')*-1
        for j in range(i):
            max_val = max(max_val, price[j] + val[i-j-1])
        val[i] = max_val
    return val[n]


@time_usage
def memoized_cut_rod(p, n):
    r = [float('inf')*-1] * (n)
    return memoized_cut_rod_aux(p,n-1,r)


def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = float('-inf')
        for i in range(1, n+1):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n-i-1, r))   # recur on length n-i
    r[n] = q
    return q

if __name__ == '__main__':
    arr = [1, 5, 8, 9, 10, 17, 17, 20]
    size = len(arr)
    memoized_cut_rod(arr, size)
    bottom_up_cut_rod(arr, size)
    calling_recursive_cut_rod(arr, size)