import pandas as pd



#df = pd.read_excel('Book1.xls', sheetname='Sheet1')
#xlsx = pd.ExcelFile('Book1.xls')
#df = pd.read_excel(xlsx, 'Sheet1')

df=pd.read_csv('s11.csv')
df.set_index('Date',inplace=True)
df.to_csv('newcsv2.csv')

df = pd.read_csv('newcsv2.csv',index_col=0)

print (df.head())
df.columns=['Austin']
print (df.head())

df.to_csv('newcsv3.csv')

df.to_html('example.html')
