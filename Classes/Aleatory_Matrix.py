import pandas as pd
import numpy as np

class Random_Matrix:

    def __init__(self, matrix, matrixError):
        self.mean = matrix
        self.std = matrixError

    def Random_Gauss(self):

        randomSample = self.mean.copy()
        for i in range(0, self.mean.shape[0]):
            for j in range(0, self.mean.shape[1]):
                randomSample.iloc[i, j] = np.random.normal(self.mean.iloc[i, j], self.std.iloc[i, j], size=1)

        return randomSample
