import numpy as np
from numpy import linalg
def matrixhit(eigen_1,eigen_2, current):
    vec_1 = eigen_1[0]
    vec_2 = eigen_2[0]
    S = np.array([[vec_1[0], vec_2[0]],[vec_1[1], vec_2[1]]])
    D = np.array([[eigen_1[1], 0],[0,eigen_2[1]]])
    return(np.matmul(S,np.matmul(D,np.matmul(np.linalg.inv(S), current))))