import pandas as pd
import pickle

#Data input
eigenvec = pd.read_csv("Output/Resultados/2D/eigenvectors2D.csv")

eigenvec.index = eigenvec["Unnamed: 0"]

eigenvec = eigenvec.drop(["Unnamed: 0"], axis=1)

eigenvecMeanDictionary = {}
eigenvecStdDictionary = {}

for k in range(0, eigenvec.shape[1]):

    with open("Input/2D/Eigenvectors/Eigenvector_"+str(k+1)+".pickle", "rb") as eigenvecFile:
        eigenvecDictionaryFile = pickle.load(eigenvecFile)

    for i in range(0, len(eigenvecDictionaryFile["Eigenvector_"+str(k+1)])):
        for j in range(0, len(eigenvecDictionaryFile["Eigenvector_"+str(k+1)][0])):
            eigenvecDictionaryFile["Eigenvector_"+str(k+1)][i][j] = pd.concat(
                eigenvecDictionaryFile["Eigenvector_"+str(k+1)][i][j], axis=1
            )

    for i in range(0, len(eigenvecDictionaryFile["Eigenvector_"+str(k+1)])):
        eigenvecDictionaryFile["Eigenvector_"+str(k+1)][i] = pd.concat(
            eigenvecDictionaryFile["Eigenvector_"+str(k+1)][i], axis=1
        )

    eigenvecMean = pd.concat(eigenvecDictionaryFile["Eigenvector_"+str(k+1)], axis=1).mean(axis=1)
    eigenvecMean = pd.DataFrame(eigenvecMean, columns=["Eigenvector"+str(k+1)+"_Mean"])

    eigenvecStd = pd.concat(eigenvecDictionaryFile["Eigenvector_"+str(k+1)], axis=1).std(axis=1)
    eigenvecStd = pd.DataFrame(eigenvecStd, columns=["Eigenvector"+str(k+1)+"_Std"])

    if "Eigenvector"+str(k+1)+"_Mean" in eigenvecMeanDictionary:
        eigenvecMeanDictionary["Eigenvector"+str(k+1)+"_Mean"].append(eigenvecMean["Eigenvector"+str(k+1)+"_Mean"])
    else:
        eigenvecMeanDictionary["Eigenvector"+str(k+1)+"_Mean"] = eigenvecMean["Eigenvector"+str(k+1)+"_Mean"]

    if "Eigenvector"+str(k+1)+"_Std" in eigenvecStdDictionary:
        eigenvecStdDictionary["Eigenvector"+str(k+1)+"_Std"].append(eigenvecStd["Eigenvector"+str(k+1)+"_Std"])
    else:
        eigenvecStdDictionary["Eigenvector"+str(k+1)+"_Std"] = eigenvecStd["Eigenvector"+str(k+1)+"_Std"]

eigenvecMean = pd.DataFrame(eigenvecMeanDictionary)
eigenvecStd = pd.DataFrame(eigenvecStdDictionary)

for i in range(0, eigenvec.shape[0]):
    for j in range(0, eigenvec.shape[1]):
        if eigenvec.iloc[i, j] > 0:
            eigenvecMean.iloc[i, j] = eigenvecMean.iloc[i, j]
        else:
            eigenvecMean.iloc[i, j] = (-1) * eigenvecMean.iloc[i, j]

# eigenvecMean.to_csv("Output/Resultados/2D/pcaMean2D.csv")
# eigenvecStd.to_csv("Output/Resultados/2D/pcaStd2D.csv")
