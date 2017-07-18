import pandas as pd
import pickle 
import matplotlib.pyplot as plt
from sodapy import Socrata
import numpy as np
from matplotlib import style
style.use('fivethirtyeight')
from time import sleep
from bokeh.plotting import *
from bokeh.models import HoverTool
from collections import OrderedDict



query=("https://openpaymentsdata.cms.gov/resource/mvzs-x4km.json")

raw_data = pd.read_json(query)	
raw_data.to_csv('n1.csv')

#api_token='Fy9CCDxku7FCGEqMx4gqi0olW'
#api_endpoint='https://opendata.socrata.com/resource/37p3-rfst.json'
#client = Socrata('data.sfgov.org', None)

#dataset_id = 'tmnf-yvry'
#dataset_id = 'k3v6-n78v'
#data = client.get(dataset_id, limit=5)
#print ('data')

#df=pd.read_csv('ownr15.csv')
#client = Socrata(api_endpoint,api_token)
#dataset_id = 'wfk4-9nvc'
#data = client.get(dataset_id,limit=2)
#df.plot()
#print(data)
#plt.show()

#cl = Socrata('https://openpaymentsdata.cms.gov/resource/9yjg-mmkd.json','Fy9CCDxku7FCGEqMx4gqi0olW', username = 'k142229@nu.edu.pk', password = 'Umer1234')
#zx = cl.get('m2u7-7eav', content_type='JSON', offset=0)

#cl = Socrata('https://openpaymentsdata.cms.gov/resource/wewi-4j5z.json','Fy9CCDxku7FCGEqMx4gqi0olW', username = 'k142229@nu.edu.pk', password = 'Umer1234')

#zx = cl.get('3d7f-ag44', limit=10, content_type='', offset=0)
#print (zx)
#zx.plot()
#plt.legend().remove()
#plt.show()