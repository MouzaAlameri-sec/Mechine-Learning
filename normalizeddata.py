
__Author__ = "Mouza Alameri"
__Date__ = "23/05/2025"
#This code is written on my birthday !!!

import pandas as pd  # for converting data into tales 
from sklearn.preprocessing import MinMaxScaler #converting values into ones and zero normalization 


import pandas as pd
from sklearn.preprocessing import MinMaxScaler

class SongDataCleaner:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.features_to_normalize = ["bpm", "nrgy", "dnce", "dB", "live", "val", 
                                      "dur", "acous", "spch", "pop"]

    def load_data(self):
        self.df = pd.read_csv(self.file_path, encoding='latin1')

    def clean_data(self):
        self.df = self.df.drop(columns=["Unnamed: 0"])
        self.df = self.df.dropna()
        self.df = self.df.drop_duplicates()

    def normalize_data(self):
        numeric_data = self.df[self.features_to_normalize]
        scaler = MinMaxScaler()
        normalized_values = scaler.fit_transform(numeric_data)
        normali


