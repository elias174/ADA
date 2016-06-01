def iterative_activity_selector(a, s, f):
    n = len(s)
    ret = [a[0]]
    k = 0
    m = 1
    while m < n:
        if s[m] >= f[k]:
            ret.append(a[m])
            k = m
        m += 1
    return ret


def recursive_activity_selector(a, s, f, k, n, ret):
    m = k
    while m < n and s[m] < f[k]:
        m += 1
    if m < n:
        ret.append(a[m])
        ret.append(recursive_activity_selector(a, s, f, m, n, ret))
        return ret
    else:
        return

s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
a = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11']
ret = []
ret.append(a[0])

print recursive_activity_selector(a, s, f, 0, 11, ret)
print iterative_activity_selector(a,s,f)