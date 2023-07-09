# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 16:34:56 2023

@author: iecet
"""

# import pandas library
import pandas as pd
  
# dictionary with list object in values
details = {
    'Name' : ['Ankit', 'Aishwarya', 'Shaurya', 'Shivangi'],
    'Age' : [23, 21, 22, 21],
    'University' : ['BHU', 'JNU', 'DU', 'BHU'],
}
  
# creating a Dataframe object 
mydf = pd.DataFrame(details)
  


