import numpy as np
matrix1=np.array(eval(input("Enter the matrix 1: ")))
matrix2=np.array(eval(input("Enter the matrix 2: ")))
mul=np.matmul(matrix1,matrix2)
print("Multiplication of two matrices: ")
print(mul)