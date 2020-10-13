from scipy.sparse import *
import numpy as np


def findDiagonal(matrix):
    
    diagonalArray = matrix.diagonal()

    return np.any(diagonalArray != 0)


def p2_has_cycle(sets):

    hasCycle = False
    matrixA = np.array(sets)
    matrixB = np.array(sets)
    matrixSize = len(matrixA)
    index = 0

    while index < matrixSize:
        
        matrixA = np.dot(matrixA, matrixB)

        if findDiagonal(matrixA) == True:
            hasCycle = True
            break

        index += 1
    
    return hasCycle