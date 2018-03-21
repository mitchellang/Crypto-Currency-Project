import numpy as np
import urllib.request
import json
import pandas as pd
import math
from pandas.io.json import json_normalize
import requests


URL0 = "https://min-api.cryptocompare.com/data/histoday?"
URL1 = "&tsym=USD&e=CCCAGG&allData=true"
#https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=USD&e=CCCAGG&allData=true
def get_coin_list():

    dataframe = pd.read_json("https://min-api.cryptocompare.com/data/all/coinlist")

    data = dataframe.Data.tolist()

    columns = list(data[0].keys())



    coins = []

    for i in data:

        try:
            coins.append(list(i.values()))

        except AttributeError:
            pass

    print(pd.DataFrame(coins))
        # try:
        #     coins.append(data.values())
        #
        # except:
        #     if math.isnan(i):
        #
        #         print(i)
        #         break

    #TODO: Expand dictionary of dataframe.Data into table



# get_coin_list()


def get_historical_price(coin_code):

    requestURL = URL0 + "fsym=" + coin_code + URL1

    dataframe = requests.get(requestURL).json()["Data"]

    result = pd.DataFrame(dataframe)

    return result

get_coin_list()

print(get_historical_price("BTC"))