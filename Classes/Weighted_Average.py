import pandas as pd

class Weighted_Average:

    def __init__(self, DataFrame, DataFrameError):
        self.data = DataFrame
        self.dataError = DataFrameError

    def Weight(self):

        weight = self.dataError.copy()
        weight = weight**2
        weight = 1/weight

        return weight

    def Average(self):

        weight = self.Weight()

        productDataWeight = self.data*weight
        sumOfWights = weight.sum(axis=0)

        sumOfProducts = productDataWeight.sum(axis=0)
        weightedAverage = pd.DataFrame(sumOfProducts/sumOfWights)

        weightedAverage.columns = [["Weighted_Average"]]

        return weightedAverage

    def Average_Error(self):

        weight = self.Weight()
        sumOfWights = weight.sum(axis=0)

        weightedAverageError = sumOfWights.apply(lambda x: (1/x)**(1/2))

        return weightedAverageError
