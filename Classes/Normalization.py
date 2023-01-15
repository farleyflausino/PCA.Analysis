import pandas as pd
import numpy as np

class Normalization:

    def __init__(self, data, deviation, diagonalMatrix, covarianceMatrix):
        self.data = data
        self.deviation = deviation
        self.diagonalMatrix = diagonalMatrix
        self.covarianceMatrix = covarianceMatrix

    def Correlation_Matrix(self):

        diagonal = np.matrix(self.diagonalMatrix)
        covariance = np.matrix(self.covarianceMatrix)

        correlation = np.matmul(diagonal, covariance)
        correlation = np.matmul(correlation, diagonal)
        correlation = pd.DataFrame(correlation)

        correlation.index = self.data.columns
        correlation.columns = self.data.columns

        return correlation

    def Normalized_Data(self):

        diagonal = np.matrix(self.diagonalMatrix)
        deviation = np.matrix(self.deviation)
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
