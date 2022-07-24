# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 20:07:23 2022

@author: sankalp
"""

import pandas as pd

# file_name = pd.read_csv('file.csv')
data = pd.read_csv('transaction.csv')
data = pd.read_csv('transaction.csv', sep=';')

# Summary of the data
data.info()

# Defining variables
CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

# Mathematical Operations on Tableau
ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem
CostPerTransaction = NumberOfItemsPurchased * CostPerItem
SellingPricePerTransaction = NumberOfItemsPurchased * SellingPricePerItem

# CostPerTransaction Column Calculation
CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

# Adding new column to dataframe
data['CostPerTransaction'] = CostPerTransaction

# Sales Per Transaction
data['SalesPerTransaction'] = data['NumberOfItemsPurchased'] * data['SellingPricePerItem']

# Mark Up = (Sale - Cost)/Cost
# Profit Calc
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']
data['MarkUp'] = data['ProfitPerTransaction'] / data['CostPerTransaction']

# Rounding MarkUp
# round(variable, digits)
data['MarkUp'] = round(data['MarkUp'], 2)

#---------

## Combining data fields (Date)
# change data type
print(data['Day'].dtype)
day = data['Day'].astype(str)
print(day.dtype)
print(data['Year'].dtype)
year = data['Year'].astype(str)
print(year.dtype)

my_date = day+'-'+data['Month']+'-'+year
data['Date'] = my_date

# using iloc to view specific columns/rows
data.iloc[0]
data.iloc[0:3]
data.iloc[:, 2] # all rows 2nd column
data.iloc[4,2]  # 4th row 2nd column

# --------

# split client key words into different columns
# new_var = column.str.split('sep', expend=True)
split_col = data['ClientKeywords'].str.split(',', expand=True)

# new column for client data
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['ClientLengthOfContract'] = split_col[2]

# using replace function, remove brackets
data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['ClientLengthOfContract'] = data['ClientLengthOfContract'].str.replace(']', '')

# lower case
data['ItemDescription'] = data['ItemDescription'].str.lower()

# bringing new data set - seasons
seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

# merging files: merge_df = pd.merge(df_old, df_new, on = 'key'), key is common feild in this case it is month
data = pd.merge(data, seasons, on = 'Month')

# dropping columns
data = data.drop('ClientKeywords', axis = 1) #column = 1
data = data.drop('Day', axis = 1)
data = data.drop(['Month', 'Year'], axis = 1)

# Export into .csv
data.to_csv('value_inc_cleaned.csv', index = False) #index = False, index will will be dropped











