import quandl
import pandas as pd



# Not necessary, I just do this so I do not show my API key.
api_key = open('quandlapikey.txt','r').read()



fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

main_df = pd.DataFrame()

for abbv in fiddy_states[0][0][1:]:
    query = "FMAC/HPI_"+str(abbv)
    df = quandl.get(query, authtoken=api_key)


   

    if main_df.empty:
        main_df = df
    else:
        main_df = pd.concat([main_df,df],axis=1)
        #main_df = main_df.join(df)

print(main_df.head())
