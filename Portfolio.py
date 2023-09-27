from Indicator import Indicator
from local_settings import *

class Portfolio:
    """
    A class representing a collection of economic indicators

    name (str): Name of portfolio
    indicators(dict): Map of indicator IDs to Indicator objects
    """
    def __init__(self, name, indicators):
        """
        Initializes a Portfolio object
        """
        self.name = name
        self.indicators = {x: Indicator(x) for x in indicators.keys()}

    def initGrowthRates(self):
        """
        Initializes growth rates for all indicators
        """
        for ind in self.indicators.values():
            ind.calcGrowthRate()

    def compareGrowthRatesForDate(self, targetDate:str):
        """
        Retrieves and prints growth rates for a given target date
        """
        for ind in self.indicators.values():
            res = ind.data.loc[ind.data['date'] == targetDate]

            print(f"{ind.id}: {ind.name}")
            if not res.empty:
                print(f"Growth Rate for [ {targetDate} ]: {res.iloc[0]['growthRate']}\n")
            else:
                print(f"No record for [ {targetDate} ]\n")

    def plotAllIndicators(self,column:str):
        """
        Plots all indicators for a given column name over time
        """
        for ind in self.indicators.values():
            ind.plotSeries(column)