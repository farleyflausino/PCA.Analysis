import pandas as pd
import numpy as np

class Random_Matrix:

    def __init__(self, matrix, matrixError):
        self.mean = matrix
        self.std = matrixError

    def Random_Gauss(self):

        sample = {}
        for i in range(0, self.mean.shape[0]):
            for j in range(0, self.mean.shape[1]):
                randomValue = np.random.normal(self.mean.iloc[i, j], self.std.iloc[i, j], size=1)
                if str(j) in sample:
                    sample[str(j)].append(randomValue)
                else:
                    sample[str(j)] = [randomValue]

        randomSample = pd.DataFrame(sample)

        return randomSample

