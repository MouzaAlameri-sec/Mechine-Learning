
import pandas as pd 
csv_file = "./data/Data.csv"
dataframe = pd.read_csv(csv_file)
print(dataframe.head())