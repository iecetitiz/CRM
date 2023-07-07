# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 14:41:58 2023

@author: iecet
"""


import datetime as dt 
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None) #butun sutunlari gor

titanic = sns.load_dataset("titanic")
car = pd.read_csv("C:/WorkSpace/PythonProjects/crm_analytics/files/car_data.csv")

titanic.columns

titanic.groupby("sex")["age"].mean()
car["Kms_Driven"].max()
car["Kms_Driven"].min()


m = titanic.groupby("sex").agg({"age": ["mean", "sum"],
                            "fare": "sum"})


titanic.groupby(["sex", "embark_town", "pclass"]).agg({"age": "mean",
                                        "survived": "mean"})


car.columns
car["Car_Name"].value_counts()

car["Car_Name"].nunique()


car["km_isleri_nasil"] = pd.cut(car["Kms_Driven"], bins = [0, 10000, 50000, 100000, 500000, 1000000])
car[car["Kms_Driven"] == 500000]


car.groupby(["Transmission", "km_isleri_nasil"]).agg({"Selling_Price": "mean"})

car.pivot_table("Selling_Price", "Transmission", "km_isleri_nasil")



for col in car.columns:
    if "er" in col:
        print(col)
















