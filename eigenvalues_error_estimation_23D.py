import pandas as pd
import pickle


#Data input
eigenval = pd.read_csv("Output/Resultados/23D/eigenvalues23D.csv")

eigenval.index = eigenval["Unnamed: 0"]

eigenval = eigenval.drop(["Unnamed: 0"], axis=1)

eigenvalMeanDictionary = {}
eigenvalStdDictionary = {}

#Eigenvalues
with open("Input/23D/Eigenvalues/Eigenvalues.pickle", "rb") as eigenvalFile:
    eigenvalDictionaryFile = pickle.load(eigenvalFile)

for i in range(0, len(eigenvalDictionaryFile["Eigenvalues"])):
    for j in range(0, len(eigenvalDictionaryFile["Eigenvalues"][0])):
        eigenvalDictionaryFile["Eigenvalues"][i][j] = pd.concat(eigenvalDictionaryFile["Eigenvalues"][i][j], axis=1)

for i in range(0, len(eigenvalDictionaryFile["Eigenvalues"])):
    eigenvalDictionaryFile["Eigenvalues"][i] = pd.concat(eigenvalDictionaryFile["Eigenvalues"][i], axis=1)

eigenvalMean = pd.concat(eigenvalDictionaryFile["Eigenvalues"], axis=1).mean(axis=1)
eigenvalMean = pd.DataFrame(eigenvalMean, columns=["Eigenvalues_Mean"])

eigenvalStd = pd.concat(eigenvalDictionaryFile["Eigenvalues"], axis=1).std(axis=1)
eigenvalStd = pd.DataFrame(eigenvalStd, columns=["Eigenvalues_Std"])

#Variance
with open("Input/23D/Eigenvalues/Variance.pickle", "rb") as varianceFile:
    varianceDictionaryFile = pickle.load(varianceFile)

for i in range(0, len(varianceDictionaryFile["Variance"])):
    for j in range(0, len(varianceDictionaryFile["Variance"][0])):
        varianceDictionaryFile["Variance"][i][j] = pd.concat(varianceDictionaryFile["Variance"][i][j], axis=1)

for i in range(0, len(varianceDictionaryFile["Variance"])):
    varianceDictionaryFile["Variance"][i] = pd.concat(varianceDictionaryFile["Variance"][i], axis=1)

varianceMean = pd.concat(varianceDictionaryFile["Variance"], axis=1).mean(axis=1)
varianceMean = pd.DataFrame(varianceMean, columns=["Variance_Mean"])

varianceStd = pd.concat(varianceDictionaryFile["Variance"], axis=1).std(axis=1)
varianceStd = pd.DataFrame(varianceStd, columns=["Variance_Std"])

#Cumulative Variance
with open("Input/23D/Eigenvalues/Cumulative_Variance.pickle", "rb") as cumulativevarianceFile:
    cumulativevarianceDictionaryFile = pickle.load(cumulativevarianceFile)

for i in range(0, len(cumulativevarianceDictionaryFile["Cumulative_Variance"])):
    for j in range(0, len(cumulativevarianceDictionaryFile["Cumulative_Variance"][0])):
        cumulativevarianceDictionaryFile["Cumulative_Variance"][i][j] = pd.concat(
            cumulativevarianceDictionaryFile["Cumulative_Variance"][i][j], axis=1
        )

for i in range(0, len(cumulativevarianceDictionaryFile["Cumulative_Variance"])):
    cumulativevarianceDictionaryFile["Cumulative_Variance"][i] = pd.concat(
        cumulativevarianceDictionaryFile["Cumulative_Variance"][i], axis=1
    )

cumulativevarianceMean = pd.concat(cumulativevarianceDictionaryFile["Cumulative_Variance"], axis=1).mean(axis=1)
cumulativevarianceMean = pd.DataFrame(cumulativevarianceMean, columns=["Cumulative_Variance_Mean"])

cumulativevarianceStd = pd.concat(cumulativevarianceDictionaryFile["Cumulative_Variance"], axis=1).std(axis=1)
cumulativevarianceStd = pd.DataFrame(cumulativevarianceStd, columns=["Cumulative_Variance_Std"])

eigenvalMean = pd.concat([eigenvalMean, varianceMean, cumulativevarianceMean], axis=1)
eigenvalStd = pd.concat([eigenvalStd, varianceStd, cumulativevarianceStd], axis=1)

eigenvalMean.to_csv("Output/Resultados/23D/eigenvalMean23D.csv")
eigenvalStd.to_csv("Output/Resultados/23D/eigenvalStd23D.csv")
