import pandas as pd
import pickle
from Classes.Weighted_Average import Weighted_Average
from Classes.Aleatory_Matrix import Random_Matrix
from Classes.Covariance import Covariance
from Classes.Normalization import Normalization
from Classes.PCA_Analysis import PCA_Analysis
from datetime import datetime

#Data input
data = pd.read_excel("Dados/Dados_PCA_29_Obs.xlsx", "Dados_29_Obs")
dataError = pd.read_excel("Dados/Dados_PCA_29_Obs.xlsx", "Incertezas_Dados_29_Obs")

data.index = data["Obs"]
dataError.index = dataError["Obs"]

data = data.drop(["Obs"], axis=1)
dataError = dataError.drop(["Obs"], axis=1)

data = data[["E(B-V)", "N(H)"]]
dataError = dataError[["E(B-V)", "N(H)"]]

#Empty dictionaries
pcaDictionary = {}
eigenvecDictionary = {}
eigenvalDictionary = {}
varianceDictionary = {}
cumulativeVarianceDictionary = {}
counter = 0

print("Inicio: "+str(datetime.now().hour)+":"+str(datetime.now().minute)+":"+str(datetime.now().second))

weightedAverage = Weighted_Average(data, dataError)

average = weightedAverage.Average()
averageError = weightedAverage.Average_Error()

covariance = Covariance(data)

random = Random_Matrix(average, averageError)

pca = PCA_Analysis()

for iteration in range(0, 10):

    #Average
    mean = random.Random_Gauss()

    #Covariance
    covarianceMatrix = covariance.Covariance_Matrix(mean)

    #Correlation
    correlation = covariance.Correlation_Matrix(mean)

    #Zscores
    Zscores = covariance.Normalized_Data(mean)

    #Eivalues and Eigenvectors
    eigenval, eigenvec = pca.Eigen(correlation)
    eigenvec = eigenvec.abs()

    # PCA Scores
    pcaScores = pca.PCA(correlation, Zscores).abs()

    #Dictionaries fill

    #PCA
    for i in range(0, pcaScores.shape[1]):

        if "PC_"+str(i+1) in pcaDictionary:
            pcaDictionary["PC_"+str(i+1)].append([pcaScores.iloc[:, i]])

        else:
            pcaDictionary["PC_" + str(i+1)] = [[pcaScores.iloc[:, i]]]

    #Eigenvector

        if "Eigenvector_" + str(i+1) in eigenvecDictionary:
            eigenvecDictionary["Eigenvector_" + str(i+1)].append([eigenvec.iloc[:,i]])
        else:
            eigenvecDictionary["Eigenvector_" + str(i+1)] = [[eigenvec.iloc[:, i]]]

    #Eigenvalues
    if "Eigenvalues" in eigenvalDictionary:
        eigenvalDictionary["Eigenvalues"].append([eigenval.iloc[:, 0]])
    else:
        eigenvalDictionary["Eigenvalues"] = [[eigenval.iloc[:, 0]]]

    #Variance
    if "Variance" in varianceDictionary:
        varianceDictionary["Variance"].append([eigenval.iloc[:, 1]])
    else:
        varianceDictionary["Variance"] = [[eigenval.iloc[:, 1]]]

    # Cumulative Variance
    if "Cumulative_Variance" in cumulativeVarianceDictionary:
        cumulativeVarianceDictionary["Cumulative_Variance"].append([eigenval.iloc[:, 2]])
    else:
        cumulativeVarianceDictionary["Cumulative_Variance"] = [[eigenval.iloc[:, 2]]]

    counter = counter + 1
    #Save in the file
    if counter == 100000:

        for i in range(0, data.shape[1]):

            #PCA
            with open("Output/2D/PCA/PC_"+str(i+1)+".pickle", "rb") as pcaFile:
                pcaDictionaryFile = pickle.load(pcaFile)

            if "PC_" + str(i+1) in pcaDictionaryFile:
                pcaDictionaryFile["PC_" + str(i+1)].append(pcaDictionary["PC_" + str(i+1)])
            else:
                pcaDictionaryFile["PC_" + str(i+1)] = [pcaDictionary["PC_" + str(i+1)]]

            with open("Output/2D/PCA/PC_"+str(i+1)+".pickle", "wb") as pcaFile:
                pickle.dump(pcaDictionaryFile, pcaFile, protocol=pickle.HIGHEST_PROTOCOL)

            #Eigenvectors
            with open("Output/2D/Eigenvectors/Eigenvector_" + str(i + 1) + ".pickle", "rb") as eigenvecFile:
                eigenvecDictionaryFile = pickle.load(eigenvecFile)

            if "Eigenvector_" + str(i + 1) in eigenvecDictionaryFile:
                eigenvecDictionaryFile["Eigenvector_" + str(i + 1)].append(
                    eigenvecDictionary["Eigenvector_" + str(i + 1)]
                )
            else:
                eigenvecDictionaryFile["Eigenvector_" + str(i + 1)] = [eigenvecDictionary["Eigenvector_" + str(i + 1)]]

            with open("Output/2D/Eigenvectors/Eigenvector_" + str(i + 1) + ".pickle", "wb") as eigenvecFile:
                pickle.dump(eigenvecDictionaryFile, eigenvecFile, protocol=pickle.HIGHEST_PROTOCOL)

        pcaDictionary = {}
        eigenvecDictionary = {}

        #Eigenvalues

        with open("Output/2D/Eigenvalues/Eigenvalues.pickle", "rb") as eigenvalFile:
            eigenvalDictionaryFile = pickle.load(eigenvalFile)

        if "Eigenvalues" in eigenvalDictionaryFile:
            eigenvalDictionaryFile["Eigenvalues"].append(eigenvalDictionary["Eigenvalues"])
        else:
            eigenvalDictionaryFile["Eigenvalues"] = [eigenvalDictionary["Eigenvalues"]]

        with open("Output/2D/Eigenvalues/Eigenvalues.pickle", "wb") as eigenvalFile:
            pickle.dump(eigenvalDictionaryFile, eigenvalFile, protocol=pickle.HIGHEST_PROTOCOL)

        eigenvalDictionary = {}

        #Variance
        with open("Output/2D/Eigenvalues/Variance.pickle", "rb") as varianceFile:
            varianceDictionaryFile = pickle.load(varianceFile)

        if "Variance" in varianceDictionaryFile:
            varianceDictionaryFile["Variance"].append(varianceDictionary["Variance"])
        else:
            varianceDictionaryFile["Variance"] = [varianceDictionary["Variance"]]

        with open("Output/2D/Eigenvalues/Variance.pickle", "wb") as varianceFile:
            pickle.dump(varianceDictionaryFile, varianceFile, protocol=pickle.HIGHEST_PROTOCOL)

        varianceDictionary = {}

        #Cumulative Variance
        with open("Output/2D/Eigenvalues/Cumulative_Variance.pickle", "rb") as cumulativeVarianceFile:
            cumulativeVarianceDictionaryFile = pickle.load(cumulativeVarianceFile)

        if "Cumulative_Variance" in cumulativeVarianceDictionaryFile:
            cumulativeVarianceDictionaryFile["Cumulative_Variance"].append(
                cumulativeVarianceDictionary["Cumulative_Variance"]
            )
        else:
            cumulativeVarianceDictionaryFile["Cumulative_Variance"] = \
                [cumulativeVarianceDictionary["Cumulative_Variance"]]

        with open("Output/2D/Eigenvalues/Cumulative_Variance.pickle", "wb") as cumulativeVarianceFile:
            pickle.dump(cumulativeVarianceDictionaryFile, cumulativeVarianceFile, protocol=pickle.HIGHEST_PROTOCOL)

        cumulativeVarianceDictionary = {}

        counter = 0

        print(
            "Fim de uma etapa de 100.000: " +
            str(datetime.now().hour) + ":" +
            str(datetime.now().minute) + ":" +
            str(datetime.now().second)
        )

print("Fim: "+str(datetime.now().hour)+":"+str(datetime.now().minute)+":"+str(datetime.now().second))