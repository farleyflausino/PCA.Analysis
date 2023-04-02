import pandas as pd
import numpy as np

class Covariance:

    def __init__(self, data):
        self.data = data

    def Covariance_Metrics(self, mean):

        deviation = self.data
        for i in range(0, self.data.shape[0]):
            for j in range(0, self.data.shape[1]):
                deviation.iloc[i, j] = self.data.iloc[i, j] - mean.iloc[j, 0]

        deviationTranspose = deviation.T
        deviationMatrix = np.matrix(deviation)
        deviationTransposeMatrix = np.matrix(deviationTranspose)
        covarianceMatrix = np.matmul(deviationTransposeMatrix, deviationMatrix)*(1 / (self.data.shape[0] - 1))

        diagonal = np.diag(covarianceMatrix)
        diagonal = diagonal**(-1/2)
        diagonalMatrix = np.diag(diagonal)

        correlation = np.matmul(diagonalMatrix, covarianceMatrix)
        correlation = np.matmul(correlation, diagonalMatrix)
        correlation = pd.DataFrame(correlation)

        correlation.index = self.data.columns
        correlation.columns = self.data.columns

        ZscoreTranspose = np.matmul(diagonalMatrix, deviationTransposeMatrix)
        Zscore = np.transpose(ZscoreTranspose)
        Zscore = pd.DataFrame(Zscore)

        ZscoreList = []

        for observation in [self.data.index]:
            ZscoreList.append("Z(" + observation + ")")

        Zscore.index = ZscoreList
        Zscore.columns = self.data.columns

        return correlation, Zscore