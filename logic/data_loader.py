import pandas as pd


def load_data():
    data = pd.read_csv('./data/Bicycle_Thefts_Open_Data.csv')
    return data
