import pandas as pd
import pickle


#Data input
pcaScores = pd.read_csv("Output/Resultados/2D/pcaScores2D.csv")

pcaScores.index = pcaScores["Obs"]

pcaScores = pcaScores.drop(["Obs"], axis=1)

pcaMeanDictionary = {}
pcaStdDictionary = {}

for k in range(0, pcaScores.shape[1]):

    with open("Input/2D/PCA/PC_"+str(k+1)+".pickle", "rb") as pcaFile:
        pcaDictionaryFile = pickle.load(pcaFile)

    for i in range(0, len(pcaDictionaryFile["PC_"+str(k+1)])):
        for j in range(0, len(pcaDictionaryFile["PC_"+str(k+1)][0])):
            pcaDictionaryFile["PC_"+str(k+1)][i][j] = pd.concat(pcaDictionaryFile["PC_"+str(k+1)][i][j], axis=1)

    for i in range(0, len(pcaDictionaryFile["PC_"+str(k+1)])):
        pcaDictionaryFile["PC_"+str(k+1)][i] = pd.concat(pcaDictionaryFile["PC_"+str(k+1)][i], axis=1)

    pcaMean = pd.concat(pcaDictionaryFile["PC_"+str(k+1)], axis=1).mean(axis=1)
    pcaMean = pd.DataFrame(pcaMean, columns=["PC"+str(k+1)+"_Mean"])

    pcaStd = pd.concat(pcaDictionaryFile["PC_"+str(k+1)], axis=1).std(axis=1)
    pcaStd = pd.DataFrame(pcaStd, columns=["PC"+str(k+1)+"_Std"])

    if "PC"+str(k+1)+"_Mean" in pcaMeanDictionary:
        pcaMeanDictionary["PC"+str(k+1)+"_Mean"].append(pcaMean["PC"+str(k+1)+"_Mean"])
    else:
        pcaMeanDictionary["PC"+str(k+1)+"_Mean"] = pcaMean["PC"+str(k+1)+"_Mean"]

    if "PC"+str(k+1)+"_Std" in pcaStdDictionary:
        pcaStdDictionary["PC"+str(k+1)+"_Std"].append(pcaStd["PC"+str(k+1)+"_Std"])
    else:
        pcaStdDictionary["PC"+str(k+1)+"_Std"] = pcaStd["PC"+str(k+1)+"_Std"]

pcaMean = pd.DataFrame(pcaMeanDictionary)
pcaStd = pd.DataFrame(pcaStdDictionary)

for i in range(0, pcaScores.shape[0]):
    for j in range(0, pcaScores.shape[1]):
        if pcaScores.iloc[i, j] > 0:
            pcaMean.iloc[i, j] = pcaMean.iloc[i, j]
        else:
            pcaMean.iloc[i, j] = (-1) * pcaMean.iloc[i, j]

pcaMean.to_csv("Output/Resultados/2D/pcaMean2D.csv")
pcaStd.to_csv("Output/Resultados/2D/pcaStd2D.csv")
