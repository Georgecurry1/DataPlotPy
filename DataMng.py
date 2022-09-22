#George Curry
from operator import index
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.options.display.max_rows=999 #sets max display for rows

foodData = pd.read_excel('sampledatafoodsales.xlsx', sheet_name='FoodSales')
print(foodData.to_string())#displays the excel file as a dataframe

dataSet = foodData[["Product","UnitPrice"]].drop_duplicates(subset='Product' ,keep='first')
#This cleans up the data and removes dups from new dataset composed of product and price

dataSet.index = ["1","2","3","4","5","6","7","8","9"]#more cleaning: this changes all indexes to be able to be iteraated orderly 
print(dataSet) #prints the cleaned up verson of new dataset

for x in range(1,9):
    #for every row in dataset, print the product,unit price(there are 9 rows within this dataset)
    formattedPrice = "{:.2f}".format(dataSet["UnitPrice"][x])#formats the price of current iteration to 2 decimals
    print(dataSet["Product"][x]+", "+str(formattedPrice))

#plot a chart
dataSet.plot(kind = "bar", x="Product", y="UnitPrice")
plt.show()