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




query=("https://openpaymentsdata.cms.gov/resource/pu3c-skbv.json")



raw_data = pd.read_json(query)	
raw_data.to_csv('o14.csv')
