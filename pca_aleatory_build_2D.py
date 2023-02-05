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

time = datetime.now()

print("Inicio: "+str(time.hour)+":"+str(time.minute)+":"+str(time.second))

for iteration in range(0, 10):

    #Covariance
    covariance = Covariance(
                            data,
                            Random_Matrix(
                                        Weighted_Average(data, dataError).Average(),
                                        Weighted_Average(data, dataError).Average_Error()
                            ).Random_Gauss()
                            )

    #Correlation
    correlation = Normalization(
                                data,
                                covariance.Deviation_Matrix(),
                                covariance.Variance_Diagonal(),
                                covariance.Covariance_Matrix()
                                )
    #Eivalues and Eigenvectors
    eigenval, eigenvec = PCA_Analysis(correlation.Normalized_Data(), correlation.Correlation_Matrix()).Eigen()
    eigenvec = eigenvec.abs()

    # Zscores
    pcaScores = PCA_Analysis(correlation.Normalized_Data(), correlation.Correlation_Matrix()).PCA().abs()

    #Dictionaries fill
    #PCA
    for i in range(pcaScores.shape[1]):
        if "PC_" + str(i+1) in pcaDictionary:
            pcaDictionary["PC_" + str(i+1)] = pd.concat(
                                                        [pcaDictionary["PC_" + str(i+1)],
                                                        pcaScores.iloc[:,i]],
                                                        axis=1
                                                        )
        else:
            pcaDictionary["PC_" + str(i+1)] = pcaScores.iloc[:, i]

    #Eigenvector
    for i in range(eigenvec.shape[1]):
        if "Eigenvector_" + str(i+1) in eigenvecDictionary:
            eigenvecDictionary["Eigenvector_" + str(i+1)] = pd.concat(
                                                                    [eigenvecDictionary["Eigenvector_" + str(i+1)],
                                                                    eigenvec.iloc[:,i]],
                                                                    axis=1
                                                                    )
        else:
            eigenvecDictionary["Eigenvector_" + str(i+1)] = eigenvec.iloc[:, i]

    #Eigenvalues
    for i in range(eigenval.shape[1]):
        if "Eigenvalues" in eigenvalDictionary:
            eigenvalDictionary["Eigenvalues"] = pd.concat(
                                                        [eigenvalDictionary["Eigenvalues"],
                                                         eigenval.iloc[:, 0]],
                                                        axis=1
                                                        )
        else:
            eigenvalDictionary["Eigenvalues"] = eigenval.iloc[:, 0]

    #Variance
        if "Variance" in varianceDictionary:
            varianceDictionary["Variance"] = pd.concat(
                                                    [varianceDictionary["Variance"],
                                                    eigenval.iloc[:, 1]],
                                                    axis=1
                                                    )
        else:
            varianceDictionary["Variance"] = eigenval.iloc[:, 1]

    #Cumulative Variance
        if "Cumulative_Variance" in cumulativeVarianceDictionary:
            cumulativeVarianceDictionary["Cumulative_Variance"] = pd.concat(
                                                                [cumulativeVarianceDictionary["Cumulative_Variance"],
                                                                 eigenval.iloc[:, 2]],
                                                                axis=1
                                                                )
        else:
            cumulativeVarianceDictionary["Cumulative_Variance"] = eigenval.iloc[:, 2]

    counter = counter + 1

    #Save in the file
    if counter == 10:

        for i in range(0, data.shape[1]):

            #PCA
            with open("Output/2D/PCA/PC_"+str(i+1)+".pickle", "rb") as pcaFile:
                pcaDictionaryFile = pickle.load(pcaFile)

            if "PC_" + str(i+1) in pcaDictionaryFile:
                pcaDictionaryFile["PC_" + str(i+1)] = pd.concat(
                                                                [pcaDictionaryFile["PC_" + str(i+1)],
                                                                pcaDictionary["PC_" + str(i+1)]],
                                                                axis=1
                                                                )
            else:
                pcaDictionaryFile["PC_" + str(i+1)] = pcaDictionary["PC_" + str(i+1)]

            with open("Output/2D/PCA/PC_"+str(i+1)+".pickle", "wb") as pcaFile:
                pickle.dump(pcaDictionaryFile, pcaFile, protocol=pickle.HIGHEST_PROTOCOL)

            #Eigenvectors
            with open("Output/2D/Eigenvectors/Eigenvector_" + str(i + 1) + ".pickle", "rb") as eigenvecFile:
                eigenvecDictionaryFile = pickle.load(eigenvecFile)

            if "Eigenvector_" + str(i + 1) in eigenvecDictionaryFile:
                eigenvecDictionaryFile["Eigenvector_" + str(i + 1)] = \
                    pd.concat(
                            [eigenvecDictionaryFile["Eigenvector_" + str(i + 1)],
                            eigenvecDictionary["Eigenvector_" + str(i + 1)]],
                            axis=1
                            )
            else:
                eigenvecDictionaryFile["Eigenvector_" + str(i + 1)] = eigenvecDictionary["Eigenvector_" + str(i + 1)]

            with open("Output/2D/Eigenvectors/Eigenvector_" + str(i + 1) + ".pickle", "wb") as eigenvecFile:
                pickle.dump(eigenvecDictionaryFile, eigenvecFile, protocol=pickle.HIGHEST_PROTOCOL)

        pcaDictionary = {}
        eigenvecDictionary = {}

        #Eigenvalues

        with open("Output/2D/Eigenvalues/Eigenvalues.pickle", "rb") as eigenvalFile:
            eigenvalDictionaryFile = pickle.load(eigenvalFile)

        if "Eigenvalues" in eigenvalDictionaryFile:
            eigenvalDictionaryFile["Eigenvalues"] = pd.concat(
                                                            [eigenvalDictionaryFile["Eigenvalues"],
                                                            eigenvalDictionary["Eigenvalues"]],
                                                            axis=1
                                                            )
        else:
            eigenvalDictionaryFile["Eigenvalues"] = eigenvalDictionary["Eigenvalues"]

        with open("Output/2D/Eigenvalues/Eigenvalues.pickle", "wb") as eigenvalFile:
            pickle.dump(eigenvalDictionaryFile, eigenvalFile, protocol=pickle.HIGHEST_PROTOCOL)

        eigenvalDictionary = {}

        #Variance
        with open("Output/2D/Eigenvalues/Variance.pickle", "rb") as varianceFile:
            varianceDictionaryFile = pickle.load(varianceFile)

        if "Variance" in varianceDictionaryFile:
            varianceDictionaryFile["Variance"] = pd.concat(
                                                            [varianceDictionaryFile["Variance"],
                                                            varianceDictionary["Variance"]],
                                                            axis=1
                                                            )
        else:
            varianceDictionaryFile["Variance"] = varianceDictionary["Variance"]

        with open("Output/2D/Eigenvalues/Variance.pickle", "wb") as varianceFile:
            pickle.dump(varianceDictionaryFile, varianceFile, protocol=pickle.HIGHEST_PROTOCOL)

        varianceDictionary = {}

        #Cumulative Variance
        with open("Output/2D/Eigenvalues/Cumulative_Variance.pickle", "rb") as cumulativeVarianceFile:
            cumulativeVarianceDictionaryFile = pickle.load(cumulativeVarianceFile)

        if "Cumulative_Variance" in cumulativeVarianceDictionaryFile:
            cumulativeVarianceDictionaryFile["Cumulative_Variance"] = pd.concat(
                                                            [cumulativeVarianceDictionaryFile["Cumulative_Variance"],
                                                            cumulativeVarianceDictionary["Cumulative_Variance"]],
                                                            axis=1
                                                            )
        else:
            cumulativeVarianceDictionaryFile["Cumulative_Variance"] = \
                cumulativeVarianceDictionary["Cumulative_Variance"]

        with open("Output/2D/Eigenvalues/Cumulative_Variance.pickle", "wb") as cumulativeVarianceFile:
            pickle.dump(cumulativeVarianceDictionaryFile, cumulativeVarianceFile, protocol=pickle.HIGHEST_PROTOCOL)

        cumulativeVarianceDictionary = {}
        counter = 0

        print("Fim de uma etapa de 100.000: " + str(time.hour) + ":" + str(time.minute) + ":" + str(time.second))

print("Fim: "+str(time.hour)+":"+str(time.minute)+":"+str(time.second))