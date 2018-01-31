import numpy as np
import urllib.request
import json
import pandas as pd


def get_coin_list():

    dataframe = pd.read_json("https://min-api.cryptocompare.com/data/all/coinlist")

    print(dataframe.Data)

    #TODO: Expand dictionary of dataframe.Data into table

get_coin_list()
