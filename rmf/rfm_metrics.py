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

df.dropna(inplace = True)

df.columns


df["InvoiceDate"].max()

today_date = dt.datetime(2010, 12, 11)

df.groupby("Customer ID").agg({"Invoice": lambda date: (today_date - date.max()).days})

smaller = df[df["Price"] < 0]

numeric = df[df["Invoice"].astype(str).str.isnumeric()]

df["TotalPrice"] = df["Price"] * df["Quantity"]

describe = df.describe().T

negative_quantitiy = df[(df["Quantity"] < 0) & ~(df["Invoice"].str.contains("C", na = False))]
negative_price = df[(df["Price"] < 0) & ~(df["Invoice"].str.contains("C", na = False))]



negative_quantitiy = df[(df["Quantity"] < 0)]


k = (df["Invoice"].astype(str).str.isnumeric())

df.info()

df["Quantity"].astype(str)

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





rfm = df.groupby("Customer ID").agg({"InvoiceDate": lambda InvoiceDate: (today_date - InvoiceDate.max()).days,
                               "Invoice": lambda invoice: invoice.nunique(),
                               "TotalPrice":  lambda totalprice: totalprice.sum()})


rfm.columns = ["recency", "frequency", "monetary"]


zero = rfm[rfm["monetary"] == 0]

rfm = rfm[rfm["monetary"] > 0]

rfm["recency_score"] = pd.qcut(rfm["recency"], 5, [5, 4, 3, 2, 1])
rfm["frequency_score"] = pd.qcut(rfm['frequency'].rank(method = "first"), 5, labels=[1, 2, 3, 4, 5])
rfm["monetary_score"] = pd.qcut(rfm['monetary'], 5, labels=[1, 2, 3, 4, 5])


###################### segmentation ###########################
rfm.columns
rfm["RFM_score"] = rfm["recency_score"].astype(str) + rfm["frequency_score"].astype(str)



# RFM isimlendirmesi
seg_map = {
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_Risk',
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customers',
    r'[4-5][2-3]': 'potential_loyalists',
    r'5[4-5]': 'champions'
}




















































































