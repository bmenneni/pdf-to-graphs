'''
Created on Dec 28, 2020

@author: bhageerath.menneni
'''
# import matplotlib.pylab as pylab
# import numpy as np
# from matplotlib import pyplot as plt

import json
import os

import csv
from re import search
AP1 = '/resources/an-page-19-table-1.json'
Andaman = '/resources/andaman-page-12-table-1.json'
#    Get the current working directory and append the file path in the resources folder
AP = os.getcwd()+AP1 
AN = os.getcwd()+Andaman#/Get this file path from the user input.
stateList = [AP, AN]
# myFile = os.getcwd()+'/resources/ap-page-125-table-1.json'
#    Opening JSON file 
for state in stateList:
    openFile = open(state)    
    #    returns JSON object as a dictionary or list
    data = json.load(openFile)
    substring = 'Children under age 5 years whose birth was registered with the civil authority'#Get this variable from the user input 
    # print(data) Iterating through the JSON list 
    #print(json.dumps(data, indent = 4, sort_keys=True))
    print(type(data))
    print(len(data))
    for indicator in data:
    #     print(indicator['0'])
        fullstring = indicator['0']
        if search(substring, fullstring):
    #    if fullstring.find(substring) != -1:
                print ("Found!")
                print(indicator['0']+" Urban:"+indicator['1']+" Rural:"+indicator['2']+" Total 2020:"+indicator['3']+" Total 20015:"+indicator['4'])
                print(indicator['3'])
#    Closing file 
openFile.close() 




# 
# 
# with open(myData) as f:
#   data = f.read()
#   indicator = json.loads(data)
# 
# # Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
#   print(json.dumps(data, indent = 4, sort_keys=True))
#   for line in data:
#     
    
  #print(data)
