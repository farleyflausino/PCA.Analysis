import pandas as pd
import numpy as np

class PCA_Analysis:

    def __init__(self, Zscore, correlation):
        self.data = Zscore
        self.correlation = correlation

    def Eigen(self):

        correlation = np.matrix(self.correlation)

        eigenvalues, eigenvectors = np.linalg.eig(correlation)

        #ordenar autovalores e autovetores
        index = eigenvalues.argsort()[::-1]
        eigenvalues = eigenvalues[index]
        eigenvectors = eigenvectors[:, index]

        eigenvalues = pd.DataFrame(eigenvalues)
        eigenvectors = pd.DataFrame(eigenvectors)

        eigenvalues.columns = [["Eigenvalues"]]

        eigenvalues["Variance"] = eigenvalues["Eigenvalues"]
        eigenvalues["Variance"] = eigenvalues["Variance"].apply(lambda x: x/float(eigenvalues["Eigenvalues"].sum()))
        eigenvalues["Cumulative_Variance"] = eigenvalues["Variance"]

        for i in range(0, eigenvalues.shape[0]):
            if i == 0:
                eigenvalues.iloc[i, 2] = eigenvalues.iloc[i, 2]
            else:
                eigenvalues.iloc[i, 2] = eigenvalues.iloc[i, 1] + eigenvalues.iloc[i-1, 2]

        listOfColumns = []
        for column in eigenvectors.columns:
            column = "Eigenvector_" + str(column+1)
            listOfColumns.append(column)

        eigenvectors.columns = listOfColumns
        eigenvectors.index = self.data.columns

        return eigenvalues, eigenvectors

    def PCA(self):

        eigenval, eigenvec = self.Eigen()

        pcaScores = np.matmul(np.matrix(self.data), np.matrix(eigenvec))

        pcaScores = pd.DataFrame(pcaScores)

        listOfColumns = []
        for column in pcaScores.columns:
            column = "PC_" + str(column + 1)
            listOfColumns.append(column)

        pcaScores.columns = listOfColumns
        pcaScores.index = self.data.index

        return pcaScores
