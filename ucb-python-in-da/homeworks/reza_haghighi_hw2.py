import numpy as np

# Include a sec4on with your name
Name = 'Reza Haghighi'

# Create matrix A with size (3,5) containing random numbers
A = np.matrix(np.random.rand(3, 5))
print(A)

# Find the size and length of matrix A
print('A Size:')
print(A.size)

print('\nA Length:')
print(len(A))

# Resize (crop) matrix A to size (3,4)
A.resize(3, 4)
print('\n3,4  A :')
print(A)

# Find the transpose of matrix A and assign it to B
print('\nMatrix B , transpose of A:')
B = A.transpose()
print(B)

# Find the minimum value in column 1 of matrix B
print('\nMax of col 1 in B:')
print(np.matrix.max(B[:, 1]))

# Find the minimum and maximum values for the en4re matrix A
print('\nMin val of B:')
print(B.min())

print('\nMax val of B:')
print(B.max())

# Create Vector X (an array) with 4 random numbers
X = np.matrix(np.random.rand(4))
print('\nX is:')
print(X)

# Create a func4on and pass Vector X and matrix A in it
def m_to_v(m, v):
    return m * v.T
    # return np.multiply(m, v)

print('\nD is:')
# In the new func4on mul4ply Vector X with matrix A and assign the result to D
D = m_to_v(A, X)
print(D)

# Create a complex number Z with absolute and real parts != 0
print('\nz is:')
Z = complex(2, 3)
print(Z)


# Show its real and imaginary parts as well as it’s absolute value
print('\nZ real is:')
print(Z.real)
print('\nZ abs is:')
print(np.absolute(Z))
print('\nZ imag is:')
print(np.imag(Z))

# Mul4ply result D with the absolute value of Z and record it to C
print('\nC is:')
C = np.multiply(D, np.absolute(Z))
print(C)

# Convert matrix B from a matrix to a string and overwrite B
B = np.str(B)
print('\nNew B is:')
print(B)

# Display a text on the screen: ‘Name is done with HW2‘, but pass your ‘Name’ as a string variable
print('\n' + Name + ' is done with HW2')









