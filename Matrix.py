from random import random, randint
class Matrix:
    def __init__(self, rows, cols, data=-1, consecutive=False):
        self.rows = rows
        self.cols = cols
        if data == -1 and consecutive == False:
            self.data = []
            for i in range(rows):
                self.data.append([])
                for j in range(cols):
                    self.data[i].append(0)
        elif consecutive == True and self.rows == 1:
            self.data = []
            temp = list(range(0, self.cols))
            self.data.append(temp)
        else:
            self.data = data

    # display matrix in readable way
    def __repr__(self):
        return self.data

    # static add method
    @staticmethod
    def add(a, b):
        result = Matrix(a.rows, a.cols)
        if type(b) is Matrix:
            if a.rows != b.rows or a.cols != b.cols:
                print("Error: Failed to add")
                return
            for i in range(a.rows):
                for j in range(a.cols):
                    result.data[i][j] = a.data[i][j] + b.data[i][j]
            return result
        elif type(b) is int:
            for i in range(a.rows):
                for j in range(a.cols):
                    result.data[i][j] += b
            return result
        else:
            print("Error: Failed to add")
            return

    @staticmethod
    def mul(a, b):
        result = Matrix(a.rows, a.cols)
        if type(b) is Matrix:
            if a.rows != b.rows or a.cols != b.cols:
                print("Error: Failed to multiply")
                return
            for i in range(a.rows):
                for j in range(a.cols):
                    result.data[i][j] = a.data[i][j] * b.data[i][j]
            return result
        elif type(b) is int:
            for i in range(a.rows):
                for j in range(a.cols):
                    result.data[i][j] *= b
            return result
        else:
            print("Error: Failed to multiply")
            return

    @staticmethod
    def sub(a, b):
        result = Matrix(a.rows, a.cols)
        if type(b) is Matrix:
            if a.rows != b.rows or a.cols != b.cols:
                print("Error: Failed to subtract")
                return
            for i in range(a.rows):
                for j in range(a.cols):
                    result.data[i][j] = a.data[i][j] * b.data[i][j]
            return result
        elif type(b) is int:
            for i in range(a.rows):
                for j in range(a.cols):
                    result.data[i][j] *= b
            return result
        else:
            print("Error: Failed to subtract")
            return

    def randomize_dec(self, upper_bound):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = random() * upper_bound

    def randomize_int(self, lower_bound, upper_bound):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = randint(lower_bound, upper_bound)

    @staticmethod
    def transpose(a):
        result = Matrix(a.cols, a.cols)
        for i in range(a.rows):
            for j in range(a.cols):
                result.data[j][i] = a.data[i][j]
        return result

    def alter(self, index: list, num: int):
        self.data[index[0]][index[1]] = num

    def to_zero(self):
        for i in self.rows:
            for j in self.cols:
                self.data[i][j] = 0

    @staticmethod
    def matMul(a, b):
        result = Matrix(a.rows, b.cols)
        if a.cols != b.rows:
            print("No. columns in A must be equal to cols in B")
            return
        for i in range(result.rows):
            for j in range(result.cols):
                sum = 0
                for k in range(a.cols):
                    sum += a.data[i][k] * b.data[k][j]
                result.data[i][j] = sum
        return result

    @staticmethod
    def apply(matrix, func):
        result = Matrix(matrix.rows, matrix.cols)
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                result.data[i][j] = func(matrix.data[i][j])
        return result