# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 22:37:45 2023

@author: iecet
"""

import datetime as dt 
import pandas as pd
pd.set_option('display.max_columns', None) #butun sutunlari gor
#pd.set_option('display.max_rows', None) #butun satirlari gor
pd.set_option('display.float_format', lambda x: '%.5f' % x) #float degerlerin noktadan sonra 5 degerini gor

df_ = pd.read_excel("files/online_retail_II.xlsx", dheet = "Year 2009-2010")
df = df_.copy()

df.columns

df["total_amount"] = df["Price"] * df['Quantity']
