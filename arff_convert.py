
import pandas as pd
import arff

df=pd.read_csv('movie_metadata.csv')

#print(df.head())
#df.to_csv('newcsv3.csv')
#df.to_arff('new1.arff')

#data = [[1,2,'a'], [3, 4, 'john']]
#arff.dump('result.arff', df, relation="whatever")
print arff.dumps(data)
