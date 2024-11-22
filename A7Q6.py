import numpy as np
matrix1=np.array(eval(input("Enter the matrix: ")))
print(matrix1)
max_row=np.amax(matrix1,axis=1)
max_col=np.amax(matrix1,axis=0)
print("Maximum values in Row wise: ",max_row)
print("Maximum values in Column wise: ",max_col)
