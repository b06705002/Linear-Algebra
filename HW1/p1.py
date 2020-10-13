from scipy.sparse import *
import numpy as np


def p1_has_cycle(sets):
        
    hasCycle = False
    matrix = np.array(sets)
    matrixSize = len(matrix)
    index = 0

    while index < matrixSize:

        midPoint = np.where(matrix[index] == 1)[0][0]
        startPoint = np.where(matrix[index] == -1)[0][0]
        index += 1
        
        for i in range(index, matrixSize):
            if matrix[i][midPoint] == -1:
                if matrix[i][startPoint] == 1:
                    hasCycle = True
                else:
                    newPath = matrix[i] + matrix[index]
                    matrix = np.append(matrix, [newPath], axis=0)

        if hasCycle == True:
            break

    return hasCycle