# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 22:37:45 2023

@author: iecet
"""

import datetime as dt 
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None) #butun sutunlari gor
#pd.set_option('display.max_rows', None) #butun satirlari gor
pd.set_option('display.float_format', lambda x: '%.2f' % x) #float degerlerin noktadan sonra 5 degerini gor

df_ = pd.read_excel("C:/WorkSpace/PythonProjects/crm_analytics/files/online_retail_II.xlsx", sheet_name = "Year 2009-2010")
df = df_.copy()

df["Invoice"].dtype
df["Invoice"]
df["Description"].dytpe
m = df.loc[0:186, "Invoice"]

df.dtypes["Invoice"]


e = df[df["Invoice"].str.contains("C")]

m.str.contains("C")
df["Invoice"].str.contains("C")



df.columns

df["total_amount"] = df["Price"] * df['Quantity']

df.groupby("Description").agg({"Quantity":"sum"}).sort_values("Quantity", ascending = False).head()

df.groupby("Invoice").agg({"total_amount": "sum"})

df.rename(columns = {'total_amount':'TotalPrice'}, inplace = True)

df.describe().T

df = df[~df["Invoice"].str.contains("C", na = False)]


# Recency, Frequency, Monetary
df.head()

df["InvoiceDate"].max()
today_date = dt.datetime(2010,12,11)

type(today_date)



rfm = df.groupby("Customer ID").agg({"InvoiceDate": lambda InvoiceDate: (today_date - InvoiceDate.max()).days,
                               "Invoice": lambda Invoice: Invoice.nunique(),
                               "TotalPrice": lambda TotalPrice: TotalPrice.sum()})


rfm.columns = ["recency", "frequency", "monetary"]


zero = rfm[rfm["monetary"] == 0]

rfm = rfm[rfm["monetary"] > 0]




rfm["frequency_score"] = pd.qcut(rfm['frequency'], 5, labels=[1, 2, 3, 4, 5])


a = [1, 2, 3, 4, 5]


head_df = df


















































