class Matrix(object):
    def __init__(self, rows, cols):
        self.rows = rows

        self.cols = cols

        self.array = [[0] * cols for i in range(rows)]

    def __add__(self, matrix):
        result = Matrix(self.rows, self.cols)

        for i in xrange(self.rows):
            for j in xrange(self.cols):
                result.array[i][j] = self.array[i][j] + matrix.array[i][j]
        return result

    def __sub__(self, matrix):
        result = Matrix(self.rows, self.cols)

        for i in xrange(self.rows):
            for j in xrange(self.cols):
                result.array[i][j] = self.array[i][j] - matrix.array[i][j]
        return result

    def __len__(self):
        return self.rows

    def __getitem__(self, x):
        return self.array[x]

    def print_mat(self):
        for i in xrange(self.rows):
            for j in xrange(self.cols):
                print self.array[i][j],
            print


def lup_solve(L, U, pi, b, y):
    n = L.rows
    x = [1] * n
    y = [1] * n
    for i in n:
        sum = 0
        for j in range(i-1):
            sum += (L[i][j] * y[j])
        y[i] = b[pi[i]] - sum
    for i in reversed(range(n)):
        sum = 0
        for j in range(i+1, n):
            sum += (U[i][j] * x[j])
        x[i] = float((y[i] - sum)) / float(U[i][i])


def lup_descomposition(A):
    n = A.rows
    pi = []
    for i in range(n):
        pi.append(i)
    for k in range(n):
        print pi
        p = 0
        for i in range(k, n):
            if abs(A[i][k]) > p:
                p = abs(A[i][k])
                k2 = i
            print p,
        if p == 0:
            return None
        pi[k], pi[k2] = pi[k2], pi[k]
        for i in range(n):
            A[k][i], A[k2][i] = A[k2][i], A[k][i]
        for i in range(k+1, n):
            A[i][k] = float(A[i][k])/float(A[k][k])
            for j in range(k+1, n):
                A[i][j] = A[i][j] - (A[i][k] * A[k][j])


def lu_decomposition(A):
    n = A.rows
    L = Matrix(n, n)
    U = Matrix(n, n)
    for i in xrange(n):
        for j in xrange(n):
            if i == j:
                L[i][j] = float(1)
    for k in range(n):
        U[k][k] = A[k][k]
        for i in range(k+1, n):
            L[i][k] = float(A[i][k])/float(U[k][k])
            U[k][i] = A[k][i]
        for i in range(k+1, n):
            for j in range(k+1, n):
                A[i][j] = A[i][j] - (L[i][k]*U[k][j])
    return L, U


A = Matrix(4, 4)
A.array = [[2, 0, 2, 0.6], [3, 3, 4, -2], [5, 5, 4, 2], [-1, -2, 3.4, -1]]
A.array = [[2, 3, 1, 5], [6, 13, 5, 19], [2, 19, 10, 23], [4, 10, 11, 31]]
print
U, L = lu_decomposition(A)
print U.print_mat()
print L.print_mat()
