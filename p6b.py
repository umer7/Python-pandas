import pandas as pd

df1 = pd.DataFrame({
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55],
                    'Year':[2001, 2002, 2003, 2004]
                    })

df3 = pd.DataFrame({
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53],
                    'Year':[2001, 2003, 2004, 2005]})


merged = pd.merge(df1,df3, on='Year', how='inner')  #left right outer
merged.set_index('Year', inplace=True)
print(merged)

#data frames that has similar data between them

#use merge when index does not matter
#join when index metter
#concatination and pending when usually to in long gates   add columns with  concatination

#apending to add to the end 
