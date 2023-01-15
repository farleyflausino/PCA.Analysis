import pandas as pd
import numpy as np

class PCA_Analysis:

    def __init__(self, Zscore, correlation):
        self.data = Zscore
        self.correlation = correlation

    def PCA(self):

        data = np.matrix(self.data)
        correlation = np.matrix(self.correlation)

        eigenvalues, eigenvectors = np.linalg.eig(correlation)

        eigenvalues = pd.DataFrame(eigenvalues)
        eigenvectors = pd.DataFrame(eigenvectors)

        return eigenvalues, eigenvectors
