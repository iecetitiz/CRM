# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 12:53:34 2023

@author: iecet
"""


# import pandas library
import pandas as pd
import numpy as np
  
# dictionary with list object in values
details = {
    'Name' : ['Ankit', 'Aishwarya', 'Shaurya', 'Shivangi', "Ece", "Melis", "nihan"],
    'Age' : [23, 21,  np.NaN, 21, 29, 20, 24],
    'University' : ['BHU', 'JNU', 'DU', 'BHU', 'DE', 12345, np.NaN]
}
  
# creating a Dataframe object 
i_df = pd.DataFrame(details)


#i_df['Age'].str.contains("Z")
  
m = i_df.dropna()



