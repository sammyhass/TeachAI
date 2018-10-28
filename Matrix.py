from random import random, randint
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = []

        for i in range(self.rows):
            self.data.append([])
            for j in range(cols):
                self.data[i].append(0)
                
    def __repr__(self):
        return_string = "Matrix(\n"
        for i in range(len(self.data)):
            return_string += str(self.data[i]) + "\n"
        return return_string + ")"

    @staticmethod
    def from_list(arr):
        m = Matrix(len(arr), 1)
        for i in range(len(arr)):
            m.data[i][0] = arr[i]
        return m
    
    def to_list(self):
        arr = []
        for i in range(self.rows):
            for j in range(self.cols):
                arr.append(self.data[i][j])
        return arr

    @staticmethod
    def transpose(a):
        result = Matrix(a.cols, a.rows)
        for i in range(a.rows):
                for j in range(a.cols):
                    result.data[j][i] = a.data[i][j]
        return result

    @staticmethod
    def multiply(a, b):
        if a.cols != b.rows:
            raise Exception("Columns of a must match rows of b")
            return
        result = Matrix(a.rows, b.cols)
        for i in range(result.rows):
            for j in range(result.cols):
                sum = 0
                for k in range(a.cols):
                    sum += a.data[i][k] * b.data[k][j]
                result.data[i][j] = sum
        return result

    @staticmethod
    def subtract(a, b):
        result = Matrix(a.rows, a.cols)
        for i in range(a.rows):
            for j in range(a.cols):
                result.data[i][j] = a.data[i][j] - b.data[i][j]
        return result

    def mul(self, n):
        if isinstance(n, Matrix):
            for i in range(len(self.data)):
                for j in range(len(self.data[i])):
                    self.data[i][j] *= n.data[i][j]
        else:
            for i in range(len(self.data)):
                for j in range(len(self.data[i])):
                    self.data[i][j] *= n

    def add(self, n):
        if isinstance(n, Matrix):
            for i in range(len(self.data)):
                for j in range(len(self.data[i])):
                    self.data[i][j] += n.data[i][j]
        else:           
            for i in range(len(self.data)):
                for j in range(len(self.data[i])):
                    self.data[i][j] += n

    def randomize(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                self.data[i][j] = random() * 2 - 1


    def map(self, func):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                val = self.data[i][j]
                self.data[i][j] = func(val)

    def map_s(a, func):
        result = Matrix(a.rows, a.cols)
        for i in range(a.rows):
            for j in range(a.cols):
                val = a.data[i][j]
                result.data[i][j] = func(val)
        return result        


