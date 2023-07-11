# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 11:04:09 2023

@author: iecet
"""


import datetime as dt
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

df_ = pd.read_excel("C:/WorkSpace/PythonProjects/crm_analytics/files/online_retail_II.xlsx", sheet_name="Year 2009-2010")

df = df_.copy()


############## veriyi hazirlama ######################################

df.isnull().sum()

df.dropna(inplace = True)

df.columns

#df = df[~df["Invoice"].str.contains("C", na = False)]

df["Invoice"].nunique()
df = df[~df["Invoice"].str.contains("C", na=False)]

type(df["Invoice"])

df["InvoiceDate"].max()
df["Decription"].value_counts()
df.groupby("Description").agg({"Quantity":"sum"})
today_date = dt.datetime(2012, 12, 11)

df["TotalPrice"] = df["Quantity"] * df["Price"]



df["Invoice"].nunique()

########################## rfm metrikleri ##################################

rfm = df.groupby("Customer ID").agg({"InvoiceDate": lambda day: (today_date - day.max()).days,
                               "Invoice" : lambda frequency: frequency.nunique(),
                               "TotalPrice": lambda totalprice: totalprice.sum()})

rfm.columns = ["recency", "frequency", "monetary"]

rfm.reset_index(inplace = False)
