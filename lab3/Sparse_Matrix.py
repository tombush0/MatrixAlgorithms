import numpy as np
import time

class CSR():
    def __init__(self, matrix):
        self.values = []
        self.col_index = []
        self.row_pointer = []
        if matrix is not None:
            self.row_pointer = [None] * matrix.shape[0]
            self.normal_to_CSR(matrix)
            # dimensions of the matrix
            self.dim = (matrix.shape[0], matrix.shape[1])

    def normal_to_CSR(self, matrix):
        for x in range(matrix.shape[0]):
            first_NZ = False
            for y in range(matrix.shape[1]):
                if matrix[x][y] != 0:
                    self.values.append(matrix[x][y])
                    self.col_index.append(y)
                    if not first_NZ:
                        self.row_pointer[x] = (len(self.values) - 1)
                        first_NZ = True
        self.row_pointer += [len(self.values)]

    def __repr__(self):
        return 'VALUES  ' + str(self.values) + '\n' + 'COL_IND ' + str(self.col_index) + '\n' + 'ROW_PTR ' + str(
            self.row_pointer)

    def to_nor(self):
        matrix = np.array([0]*(self.dim[0]*self.dim[1])).reshape(self.dim[0],self.dim[1])
        row_ptr = self.row_pointer[0]
        row_ptr_index = 0
        for i in range(len(self.values)):
            if i is self.row_pointer[row_ptr_index+1]:
                row_ptr += 1
                row_ptr_index+=1
            # print('row', row_ptr, 'col', self.col_index[i], 'val', self.values[i])
            matrix[row_ptr][self.col_index[i]] = self.values[i]

        return matrix

    def CSR_to_CSC(self):
        NNZ = len(self.values)
        row_index, csc_values = [0]*NNZ, [0]*NNZ
        col_pointer = [0]* (self.dim[1])

        a = self.values
        ia = self.row_pointer + [NNZ]
        ja = self.col_index
        ao = csc_values
        iao = row_index
        jao = col_pointer
        n = self.dim[0]

        for i in range(n):
            for k in range(ia[i], ia[i+1]):
                j = ja[k]
                next = iao[j]
                ao[next] = a[k]

                jao[next] = i
                iao[j] = next+1

        for i in range(n, 0, -1):
            iao[i+1] = iao[i]

        csc_values = ao
        row_index = iao
        col_pointer = jao
        result = CSC(None)
        result.values = csc_values
        result.row_index = row_index
        result.col_pointer = col_pointer

        return CSC(self.to_nor())


class CSC():

    def __init__(self, matrix):
        self.values = []
        self.pointer = []
        self.row_index = []
        if matrix is not None:
            self.col_pointer = [None] * matrix.shape[1]
            self.normal_to_CSC(matrix)
            # dimensions of the matrix
            self.dim = (matrix.shape[0], matrix.shape[1])

    def normal_to_CSC(self, matrix):
        for y in range(matrix.shape[1]):
            first_NZ = False
            for x in range(matrix.shape[0]):
                if matrix[x][y] != 0:
                    self.values.append(matrix[x][y])
                    self.row_index.append(x)
                    if not first_NZ:
                        self.col_pointer[y] = (len(self.values) - 1)
                        first_NZ = True
        self.col_pointer += [len(self.values)]

    def __repr__(self):
        return 'VALUES  '  + str(self.values) + '\n' + 'ROW_IND ' + str(self.row_index) + '\n' + 'COL_PTR ' + str(self.col_pointer)

    def __eq__(self, other):
        c_1 = (self.values == other.values)
        c_2 = (self.col_pointer == other.col_pointer)
        c_3 = (self.row_index == other.row_index)
        return c_1 and c_2 and c_3

    def to_normal(self):
        matrix = np.array([0] * (self.dim[0] * self.dim[1])).reshape(self.dim[0], self.dim[1])
        col_ptr = self.col_pointer[0]
        col_ptr_index = 0
        for i in range(len(self.values)):
            if i is self.col_pointer[col_ptr_index + 1]:
                col_ptr += 1
                col_ptr_index += 1
            matrix[self.row_index[i]][col_ptr] = self.values[i]

        return matrix



A = np.array([[1, 1, 0], [0, 1, 0], [-1, 0, 3]])

print(A, '\n')
A_csr = CSR(A)
A_csc = CSC(A)

print(A_csr,'\n')

# converting CSR to CSC
# A_converted = A_csr.CSR_to_CSC()
# print(A_converted, '\n')
#
# print(A_csc)
#
# # is the result correct
# print(A_csc == A_converted)


