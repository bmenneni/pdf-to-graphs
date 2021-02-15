'''
Created on Dec 25, 2020

@author: ravi.menneni
'''
import os
import pandas as pd
from matplotlib import pyplot as plt
import csv




myData = os.getcwd()+'/resources/tl-page-126-table-1.csv'

# data = pd.read_csv(myData)
# #data.head()
# df = pd.DataFrame(data)
# #df
# print(df['Unnamed: 1'])
with open(myData) as f:
    csv_reader = csv.DictReader(f)
    for line in csv_reader:
        
       fullString = line.get("None", {'x': None}).get("Indicator")
       print(fullString)
       
       subString = '41. Mothers who had at least 4 antenatal care visits (%)'
       print(subString)
       
#        if subString in fullString:
#             print ("I got it: Found!")
#        else:
#             print ("Not found!")
       
            