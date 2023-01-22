import pandas as pd
import pickle


#Data input
eigenvec = pd.read_csv("Output/Resultados/2D/eigenvectors2D.csv")

eigenvec.index = eigenvec["Unnamed: 0"]

eigenvec = eigenvec.drop(["Unnamed: 0"], axis=1)

eigenvecMeanDictionary = {}
eigenvecStdDictionary = {}

for i in range(0, eigenvec.shape[1]):

    with open("Input/2D/Eigenvectors/Eigenvector_"+str(i+1)+".pickle", "rb") as eigenvecFile:
        eigenvecDictionaryFile = pickle.load(eigenvecFile)

    eigenvecMeanDictionary["Eigenvector_"+str(i+1)] = eigenvecDictionaryFile["Eigenvector_"+str(i+1)].mean(axis=1)
    eigenvecStdDictionary["Eigenvector_"+str(i+1)] = eigenvecDictionaryFile["Eigenvector_"+str(i+1)].std(axis=1)


eigenvecMean = pd.DataFrame.from_dict(eigenvecMeanDictionary)
eigenvecStd = pd.DataFrame.from_dict(eigenvecStdDictionary)

for i in range(0, eigenvec.shape[0]):
    for j in range(0, eigenvec.shape[1]):
        if eigenvec.iloc[i, j] < 0:
            eigenvecMean.iloc[i, j] = (-1)*eigenvecMean.iloc[i, j]
        else:
            eigenvecMean.iloc[i, j] = eigenvecMean.iloc[i, j]

# eigenvecMean.to_csv("Output/Resultados/2D/pcaMean2D.csv")
# eigenvecStd.to_csv("Output/Resultados/2D/pcaStd2D.csv")
