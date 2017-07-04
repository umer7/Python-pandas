#buliding data sets

import quandl
import pandas as pd

#api_key = open('Sa1UpSiV8bM1y7xC6XRt','r').read()
#df = quandl.get("FMAC/HPI_AK",authtoken=api_key)


#df = quandl.get("FMAC/HPI_VT", collapse="quarterly")
#print(df.head())

states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
#this is list
#print(states)

#this is dataframe
#print(states[0])

#this is column
print(states[0][0])

for abbv in states [0][0][1:]:
    print("FMAC/HPI"+str(abbv))

	
