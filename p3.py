#insert excel file
#pip install openpyxl
import pandas as pd
dataframe = pd.read_excel('Datasets.xlsx')
dataframe.to_excel('Datasets.xlsx')

print(dataframe.head())
