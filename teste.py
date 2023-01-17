import pandas as pd
import numpy as np

data = pd.read_excel("Dados/Dados_PCA_29_Obs.xlsx", "Dados_29_Obs")
dataError = pd.read_excel("Dados/Dados_PCA_29_Obs.xlsx", "Incertezas_Dados_29_Obs")

data.index = data["Obs"]
dataError.index = dataError["Obs"]

data = data.drop(["Obs"], axis=1)
dataError = dataError.drop(["Obs"], axis=1)

# data = data[["E(B-V)", "N(H)"]]
# dataError = dataError[["E(B-V)", "N(H)"]]


from Classes.Weighted_Average import Weighted_Average

weighted_average = Weighted_Average(data, dataError)

weight = weighted_average.Weight()

weightedAverage = weighted_average.Average()

from Classes.Covariance import Covariance

covariance = Covariance(data, weightedAverage)

covarianceMatrix = covariance.Covariance_Matrix()

diagonalMatrix = covariance.Variance_Diagonal()

deviation = covariance.Deviation_Matrix()

from Classes.Normalization import Normalization

normalization = Normalization(data, deviation, diagonalMatrix, covarianceMatrix)

correlationMatrix = normalization.Correlation_Matrix()
normalizedData = normalization.Normalized_Data()

from Classes.PCA_Analysis import PCA_Analysis

pca = PCA_Analysis(normalizedData, correlationMatrix)

eigenval, eigenvec = pca.Eigen()