import pandas as pd
import pickle


data = pd.read_excel("Dados/Dados_PCA_29_Obs.xlsx", "Dados_29_Obs")
data = data[["E(B-V)", "N(H)"]]

pcaDictionaryFile = {}
eigenvecDictionaryFile = {}
eigenvalDictionaryFile = {}
varianceDictionaryFile = {}
cumulativeVarianceDictionaryFile = {}

for i in range(0, data.shape[1]):

    with open("Output/2D/PCA/PC_"+str(i+1)+".pickle", "wb") as pcaFile:
        pickle.dump(pcaDictionaryFile, pcaFile)

    with open("Output/2D/Eigenvectors/Eigenvector_"+str(i+1)+".pickle", "wb") as eigenvecFile:
        pickle.dump(eigenvecDictionaryFile, eigenvecFile)

with open("Output/2D/Eigenvalues/Eigenvalues.pickle", "wb") as eigenvalFile:
    pickle.dump(eigenvalDictionaryFile, eigenvalFile)

with open("Output/2D/Eigenvalues/Variance.pickle", "wb") as varianceFile:
    pickle.dump(varianceDictionaryFile, varianceFile)

with open("Output/2D/Eigenvalues/Cumulative_Variance.pickle", "wb") as cumulativeVarianceFile:
    pickle.dump(cumulativeVarianceDictionaryFile, cumulativeVarianceFile)