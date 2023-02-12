import pandas as pd
import numpy as np

class Covariance:

    def __init__(self, data):
        self.data = data

    def Deviation_Matrix(self, average):

        deviation = self.data.copy()
        for i in range(0, self.data.shape[0]):
            for j in range(0, self.data.shape[1]):
                deviation.iloc[i, j] = self.data.iloc[i, j] - average.iloc[j, 0]

        return deviation


    def Covariance_Matrix(self, average):

        deviation = self.Deviation_Matrix(average)

        deviationTranspose = deviation.T
        deviationMatrix = np.matrix(deviation)
        deviationTransposeMatrix = np.matrix(deviationTranspose)
        covarianceMatrix = np.matmul(deviationTransposeMatrix, deviationMatrix)*(1 / (self.data.shape[0] - 1))

        covarianceMatrix = pd.DataFrame(covarianceMatrix)
        # covarianceMatrix = covarianceMatrix * (1 / (self.data.shape[0] - 1))

        covarianceMatrix.index = self.data.columns
        covarianceMatrix.columns = self.data.columns

        return covarianceMatrix

    def Variance_Diagonal(self, average):

        covarianceMatrix = self.Covariance_Matrix(average)

        covarianceMatrix = np.matrix(covarianceMatrix)
        diagonal = np.diag(covarianceMatrix)
        diagonal = diagonal**(-1/2)
        diagonalMatrix = np.diag(diagonal)
        diagonalMatrix = pd.DataFrame(diagonalMatrix)

        diagonalMatrix.index = self.data.columns
        diagonalMatrix.columns = self.data.columns

        return diagonalMatrix

    def Correlation_Matrix(self, average):

        diagonal = np.matrix(self.Variance_Diagonal(average))
        covariance = np.matrix(self.Covariance_Matrix(average))

        correlation = np.matmul(diagonal, covariance)
        correlation = np.matmul(correlation, diagonal)
        correlation = pd.DataFrame(correlation)

        correlation.index = self.data.columns
        correlation.columns = self.data.columns

        return correlation

    def Normalized_Data(self, average):

        diagonal = np.matrix(self.Variance_Diagonal(average))
        deviation = np.matrix(self.Deviation_Matrix(average))
        deviationTranspose = np.transpose(deviation)

        ZscoreTranspose = np.matmul(diagonal, deviationTranspose)
        Zscore = np.transpose(ZscoreTranspose)
        Zscore = pd.DataFrame(Zscore)

        ZscoreList = []

        for observation in [self.data.index]:
            ZscoreList.append("Z(" + observation + ")")

        Zscore.index = ZscoreList
        Zscore.columns = self.data.columns

        return Zscore