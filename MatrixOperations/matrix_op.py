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
    x = []
    for i in n:
        pass


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


A = Matrix(4, 4)
A.array = [[2, 0, 2, 0.6], [3, 3, 4, -2], [5, 5, 4, 2], [-1, -2, 3.4, -1]]
A.print_mat()
print
lup_descomposition(A)
print
print
A.print_mat()