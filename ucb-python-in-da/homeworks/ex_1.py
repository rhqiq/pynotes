import numpy as np


class _FileOperations:

    @staticmethod
    def write_my_file(arr):
        arr.tofile('ex_1.txt', ',')

    @staticmethod
    def read_my_file():
        file = open('ex_1.txt', 'r')
        return file.readlines()[0]


arr = np.arange(5, 45, 7)
_FileOperations.write_my_file(arr)

s_arr = _FileOperations.read_my_file()

arr_c = np.array(s_arr.split(","), dtype='int16')

mx = np.matrix([[1], [2], [3]], dtype='int16')

_FileOperations.write_my_file(np.multiply(mx, arr_c))

s_mx = _FileOperations.read_my_file()

mx_c = np.array(s_mx.split(","), dtype='int16').reshape(3, 6)

print(mx_c)













