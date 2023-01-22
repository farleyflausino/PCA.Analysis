import pandas as pd
import pickle


#Data input
eigenval = pd.read_csv("Output/Resultados/2D/eigenvalues2D.csv")

eigenval.index = eigenval["Unnamed: 0"]

eigenval = eigenval.drop(["Unnamed: 0"], axis=1)

eigenvalMeanDictionary = {}
eigenvalStdDictionary = {}

with open("Input/2D/Eigenvalues/Eigenvalues.pickle", "rb") as eigenvalFile:
    eigenvalDictionaryFile = pickle.load(eigenvalFile)

eigenvalMeanDictionary["Eigenvalues"] = eigenvalDictionaryFile["Eigenvalues"].mean(axis=1)
eigenvalStdDictionary["Eigenvalues"] = eigenvalDictionaryFile["Eigenvalues"].std(axis=1)

with open("Input/2D/Eigenvalues/Variance.pickle", "rb") as varianceFile:
    varianceDictionaryFile = pickle.load(varianceFile)

eigenvalMeanDictionary["Variance"] = varianceDictionaryFile["Variance"].mean(axis=1)
eigenvalStdDictionary["Variance"] = varianceDictionaryFile["Variance"].std(axis=1)

with open("Input/2D/Eigenvalues/Cumulative_Variance.pickle", "rb") as cumulativeVarianceFile:
    cumulativeVarianceDictionaryFile = pickle.load(cumulativeVarianceFile)

eigenvalMeanDictionary["Cumulative_Variance"] = cumulativeVarianceDictionaryFile["Cumulative_Variance"].mean(axis=1)
eigenvalStdDictionary["Cumulative_Variance"] = cumulativeVarianceDictionaryFile["Cumulative_Variance"].std(axis=1)

eigenvalMean = pd.DataFrame.from_dict(eigenvalMeanDictionary)
eigenvalStd = pd.DataFrame.from_dict(eigenvalStdDictionary)


# eigenvalMean.to_csv("Output/Resultados/2D/eigenvalMean2D.csv")
# eigenvalStd.to_csv("Output/Resultados/2D/eigenvalStd2D.csv")