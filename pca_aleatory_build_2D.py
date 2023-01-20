import pandas as pd
import numpy as np
import pickle
from Classes.Weighted_Average import Weighted_Average
from Classes.Covariance import Covariance
from Classes.Normalization import Normalization
from Classes.PCA_Analysis import PCA_Analysis

#Data input
data = pd.read_excel("Dados/Dados_PCA_29_Obs.xlsx", "Dados_29_Obs")
dataError = pd.read_excel("Dados/Dados_PCA_29_Obs.xlsx", "Incertezas_Dados_29_Obs")

data.index = data["Obs"]
dataError.index = dataError["Obs"]

data = data.drop(["Obs"], axis=1)
dataError = dataError.drop(["Obs"], axis=1)

data = data[["E(B-V)", "N(H)"]]
dataError = dataError[["E(B-V)", "N(H)"]]

mean = Weighted_Average(data, dataError)

average = mean.Average()
averageError = mean.Average_Error()

#Criar uma classe que aplique a função random em cada elemento do vetor de média através da função lambda
# aleatoryMean = np.random.normal(mean.Average(), mean.Average_Error())






