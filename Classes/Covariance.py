import pandas as pd
import numpy as np

class Covariance:

    def Deviation_Matrix(self, data, average):

        deviation = data.copy()
        for i in range(0, data.shape[0]):
            for j in range(0, data.shape[1]):
                deviation.iloc[i, j] = data.iloc[i, j] - average.iloc[j, 0]

        return deviation


    def Covariance_Matrix(self, data, average):

        deviation = self.Deviation_Matrix(data, average)

        deviationTranspose = deviation.T
        deviationMatrix = np.matrix(deviation)
        deviationTransposeMatrix = np.matrix(deviationTranspose)
        covarianceMatrix = np.matmul(deviationTransposeMatrix, deviationMatrix)

        covarianceMatrix = pd.DataFrame(covarianceMatrix)
        covarianceMatrix = covarianceMatrix * (1 / (data.shape[0] - 1))

        covarianceMatrix.index = data.columns
        covarianceMatrix.columns = data.columns

        return covarianceMatrix

    def Variance_Diagonal(self, data, average):

        covarianceMatrix = self.Covariance_Matrix(data, average)

        covarianceMatrix = np.matrix(covarianceMatrix)
        diagonal = np.diag(covarianceMatrix)
        diagonal = diagonal**(-1/2)
        diagonalMatrix = np.diag(diagonal)
        diagonalMatrix = pd.DataFrame(diagonalMatrix)

        diagonalMatrix.index = data.columns
        diagonalMatrix.columns = data.columns

        return diagonalMatrix
