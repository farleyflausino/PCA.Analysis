import pandas as pd
import numpy as np

class Covariance:
    def __init__(self, data, average):
        self.data = data
        self.average = average

    def Deviation_Matrix(self):

        deviation = self.data.copy()
        for i in range(0, self.data.shape[0]):
            for j in range(0, self.data.shape[1]):
                deviation.iloc[i, j] = self.data.iloc[i, j] - self.average.iloc[j, 0]

        return deviation


    def Covariance_Matrix(self):

        deviation = self.Deviation_Matrix()

        deviationTranspose = deviation.T
        deviationMatrix = np.matrix(deviation)
        deviationTransposeMatrix = np.matrix(deviationTranspose)
        covarianceMatrix = np.matmul(deviationTransposeMatrix, deviationMatrix)

        covarianceMatrix = pd.DataFrame(covarianceMatrix)
        covarianceMatrix = covarianceMatrix * (1 / (self.data.shape[0] - 1))

        covarianceMatrix.index = self.data.columns
        covarianceMatrix.columns = self.data.columns

        return covarianceMatrix

    def Variance_Diagonal(self):

        covarianceMatrix = self.Covariance_Matrix()

        covarianceMatrix = np.matrix(covarianceMatrix)
        diagonal = np.diag(covarianceMatrix)
        diagonal = diagonal**(-1/2)
        diagonalMatrix = np.diag(diagonal)
        diagonalMatrix = pd.DataFrame(diagonalMatrix)

        diagonalMatrix.index = self.data.columns
        diagonalMatrix.columns = self.data.columns

        return diagonalMatrix
