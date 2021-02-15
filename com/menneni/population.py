'''
Created on Dec 22, 2020

@author: ravi.menneni
'''
import os
import json
import PyPDF2
#from aifc import data
#Read File
print(os.getcwd())
# myJsonFile = open(os.getcwd()+"/resources/jsonFile.json", "r")
# jasonData = myJsonFile.read()
# #Parse
# myJsonObject = json.loads(jasonData)
# print(str(myJsonObject["firstName"]))
# 
# addressList = myJsonObject["Address"]
# print(addressList[0].get("city"))
# 
# for i in range(len(addressList)):
#     print(addressList[i].get("city"))
#     print(addressList[i].get("state"))
#     print(addressList[i].get("country"))

# data = {"iowa": "3m", "Nebraska": "2m"}
# print(data.get("iowa"))

from PyPDF2 import PdfFileReader
 
myPdf = os.getcwd()+"/resources/nfhs5.pdf"

reader = PdfFileReader(myPdf)
page127 = reader.getPage(127)

Tdata = page127.extractText()
print(Tdata)



