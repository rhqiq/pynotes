# import numpy
import numpy as np
# import random module and matrix type
from numpy import random, matrix

# 1. Include a section with your name
# Student name: Pedram Tadyaoni
# Course Name: Python for Data Analysis and Scientific Computing
print('\n1. Student Name: Pedram Tadayoni\n Course Name:Python for Data Analysis and Scientific Computing\n')

# 2. Create matrix A with size (3,5) containing random numbers
# generate 15 random numbers and put them into an one line array
A = random.random(15)

# reshape the one line array into an array with 3 rows and 5 columns
A = A.reshape(3,5)

# convert the array to a matrix
A = matrix(A)
print('\n2. Matrix A with size (3,5) containing random numbers:\n', A, '\n')

# 3. Find the size and length of matrix A
sz = A.size
print('\n3. Size of Matrix A --> ', sz, '\n')

# 4. Resize (crop) matrix A to size (3,4)
A.resize(3,4)
print('\n4. Matrix A resized to size(3,4):\n', A,'\n')

# 5. Find the transpose of matrix A and assign it to B
B = A.T
print('\n5. Matrix A transposed and assinged to B:\n', B, '\n')

# 6. Find the minimum value in column 1 of matrix B 
# Column index starts from 0 thus column 1 is 2nd column.
# B[:,1] returns a slice of A which is the column2(2nd column), 'min' function returns the smallest number from the sliced matrix.
mnB = min(B[:,1])
print('\n6. Minimum of column 1 of Matrix B --> ', mnB, '\n')

# 7 Find the minimum and maximum values for the entire matrix A
# Find the minimum of the matrix A
mnA = A.min()
print('\n7.1. Minimum value in matrix A --> ', mnA, '\n')

# Find the maximum of the matrix A
mxA = A.max()
print('\n7.2. Maximum value in matrix A --> ', mxA, '\n')


# 8. Create Vector X (an array) with 4 random numbers.
X = random.random(4)
X = np.matrix(X)
print('\n8. Vector X with 4 random numbers:\n', X, '\n')

# 9. Create a function and pass Vector X and matrix A in it
# 10. In the new function muliply Vector X with matrix A and assign the result to D
def multiplyMatrixByVector(mtrx, vctr):
    return mtrx * vctr.T  # If 'A' Matrix and 'X' Vector are multiplied we get an error that shapes (3,4) and (1,4) are not aligned thus we should align the shpaes first by transposing the 'X' vetor

D = multiplyMatrixByVector(A, X)
print('\n9. and 10.  \'A\' matrix multiplied by \'X\' vector:\n', D, '\n')

# 11. Create a complex number Z with absolute and real parts != 0
# 12. Show its real and imaginary parts as well as it’s absolute value
Z = complex(2, 3)
print('\n10. and 11. Absolue value of Z --> ', Z)
print('\n12.1 Real part of Z --> ', Z.real)
print('\n12.2 Imaginary part of Z --> ', Z.imag)

# 13. Muliply result D with the absolute value of Z and record it to C
C = D * Z
print('\n13. Z multipled by D:\n', C, '\n')

# 14. Convert matrix B from a matrix to a string and overwrite B
B = np.str(B)
print('\n14. B matrix converted to string:\n', B, '\n')

# 15. Display a text on the screen: ‘Name is done with HW2‘, but pass your ‘Name’ as a string variable
nameStr= 'Pedram'
print('\n15. Display text on screen:')
print("%s is done with HW2" % nameStr)