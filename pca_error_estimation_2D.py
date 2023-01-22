import pandas as pd
import pickle


#Data input
pcaScores = pd.read_csv("Output/Resultados/2D/pcaScores2D.csv")

pcaScores.index = pcaScores["Obs"]

pcaScores = pcaScores.drop(["Obs"], axis=1)

pcaMeanDictionary = {}
pcaStdDictionary = {}

for i in range(0, pcaScores.shape[1]):

    with open("Input/2D/PCA/PC_"+str(i+1)+".pickle", "rb") as pcaFile:
        pcaDictionaryFile = pickle.load(pcaFile)

    pcaMeanDictionary["PC_"+str(i+1)] = pcaDictionaryFile["PC_"+str(i+1)].mean(axis=1)
    pcaStdDictionary["PC_"+str(i+1)] = pcaDictionaryFile["PC_"+str(i+1)].std(axis=1)


pcaMean = pd.DataFrame.from_dict(pcaMeanDictionary)
pcaStd = pd.DataFrame.from_dict(pcaStdDictionary)

for i in range(0, pcaScores.shape[0]):
    for j in range(0, pcaScores.shape[1]):
        if pcaScores.iloc[i, j] < 0:
            pcaMean.iloc[i, j] = (-1)*pcaMean.iloc[i, j]
        else:
            pcaMean.iloc[i, j] = pcaMean.iloc[i, j]

# pcaMean.to_csv("Output/Resultados/2D/pcaMean2D.csv")
# pcaStd.to_csv("Output/Resultados/2D/pcaStd2D.csv")
