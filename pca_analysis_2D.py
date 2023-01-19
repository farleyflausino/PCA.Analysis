import pandas as pd
from Classes.Weighted_Average import Weighted_Average
from Classes.Covariance import Covariance
from Classes.Normalization import Normalization
from Classes.PCA_Analysis import PCA_Analysis

data = pd.read_excel("Dados/Dados_PCA_29_Obs.xlsx", "Dados_29_Obs")
dataError = pd.read_excel("Dados/Dados_PCA_29_Obs.xlsx", "Incertezas_Dados_29_Obs")

data.index = data["Obs"]
dataError.index = dataError["Obs"]

data = data.drop(["Obs"], axis=1)
dataError = dataError.drop(["Obs"], axis=1)

data = data[["E(B-V)", "N(H)"]]
dataError = dataError[["E(B-V)", "N(H)"]]

average = Weighted_Average(data, dataError)

covariance = Covariance(data, average.Average())

normalization = Normalization(data,
                              covariance.Deviation_Matrix(),
                              covariance.Variance_Diagonal(),
                              covariance.Covariance_Matrix()
                              )

Zscores = normalization.Normalized_Data()

pca = PCA_Analysis(Zscores, normalization.Correlation_Matrix())

eigenval, eigenvec = pca.Eigen()

pcaScores = pca.PCA()

eigenval.to_csv("Output/Resultados/2D/eigenvalues2D.csv")
eigenvec.to_csv("Output/Resultados/2D/eigenvectors2D.csv")
Zscores.to_csv("Output/Resultados/2D/Zscores2D.csv")
pcaScores.to_csv("Output/Resultados/2D/pcaScores2D.csv")
