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


def matrix_product(A, B):
    n = len(A)
    C = Matrix(n, n)
    for i in xrange(n):
        for k in xrange(n):
            for j in xrange(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def strassen(A, B):
    n = len(A)
    if n == 1:
        return matrix_product(A, B)

    else:
        new_size = n/2
        a11 = Matrix(new_size, new_size)
        a12 = Matrix(new_size, new_size)
        a21 = Matrix(new_size, new_size)
        a22 = Matrix(new_size, new_size)

        b11 = Matrix(new_size, new_size)
        b12 = Matrix(new_size, new_size)
        b21 = Matrix(new_size, new_size)
        b22 = Matrix(new_size, new_size)

        for i in xrange(0, new_size):
            for j in xrange(0, new_size):
                a11[i][j] = A[i][j]
                a12[i][j] = A[i][j + new_size]
                a21[i][j] = A[i + new_size][j]
                a22[i][j] = A[i + new_size][j + new_size]

                b11[i][j] = B[i][j]
                b12[i][j] = B[i][j + new_size]
                b21[i][j] = B[i + new_size][j]
                b22[i][j] = B[i + new_size][j + new_size]

        s1 = b12 - b22
        s2 = a11 + a12
        s3 = a21 + a22
        s4 = b21 - b11
        s5 = a11 + a22
        s6 = b11 + b22
        s7 = a12 - a22
        s8 = b21 + b22
        s9 = a11 - a21
        s10 = b11 + b12

        p1 = strassen(a11, s1)
        p2 = strassen(s2, b22)
        p3 = strassen(s3, b11)
        p4 = strassen(a22, s4)
        p5 = strassen(s5, s6)
        p6 = strassen(s7, s8)
        p7 = strassen(s9, s10)

        c11 = p4 + p5 + p6 - p2
        c12 = p1 + p2
        c21 = p3 + p4
        c22 = p1 + p5 - p3 - p7

        # Rearmar matriz
        result = Matrix(n, n)
        for i in xrange(0, new_size):
            for j in xrange(0, new_size):
                result[i][j] = c11[i][j]
                result[i][j + new_size] = c12[i][j]
                result[i + new_size][j] = c21[i][j]
                result[i + new_size][j + new_size] = c22[i][j]
        return result

A = Matrix(2, 2)
A.array = [[2, 3], [1, 2], ]

B = Matrix(2, 2)
B.array = [[1, 6], [5, 7], ]

print strassen(A, B).array