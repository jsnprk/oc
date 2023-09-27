import fredapi as fa
import pandas as pd
import matplotlib.pyplot as mpl
import numpy as np
from bs4 import BeautifulSoup, NavigableString
import requests
from local_settings import *

class Indicator:
    """
    A class representing an economic indicator from the FRED API

    Attributes:
        id (str): Unique identifier on FRED
        name (str): Title/Description of indicator
        data (DataFrame): Time series data
    """
    def __init__(self, id, name = None, data = None):
        """
        Initializes Indicator object
        """
        self.id = id

        if name is None:
            name = self.seriesNameLookup(id)
        self.name = name

        if data is None:
            fred = fa.Fred(api_key=fred_api_key)
            series = fred.get_series(id)
            data = pd.DataFrame( { 'date' : series.index, 'value' : series.values } )
        self.data = data

    def seriesNameLookup(self, id: int) -> str:
        """
        Retrieves name of indicator for a given ID via web scraping
        """
        page = requests.get(f'https://fred.stlouisfed.org/series/{id}', headers = HEADER)
        page.raise_for_status()

        soup = BeautifulSoup(page.content, "lxml")
        div = soup.find("div", {'class':'series-title'})
        title = [elem for elem in div.h1 if isinstance(elem, NavigableString)]
        return(title[0])

    def calcGrowthRate(self):
        """
        Calculates and creates a new 'growthRate' column
        """
        self.data['growthRate'] = np.round(self.data['value'].pct_change()*100,2)    

    def plotSeries(self,column:'str'):
        """
        Plots specified column over time
        """
        mpl.plot(self.data["date"],self.data[column])
        mpl.show()