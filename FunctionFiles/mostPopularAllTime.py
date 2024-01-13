#!/usr/bin/env python3

#Outputs the 10 most popular names of all time from one dataset (over all years)

# Libraries
import os
import sys
import getopt
import csv
import pandas as pd

#given dataSet is a copy, feel free to change around values
def mostPopularAllTime(dataSet):

  #Reads data set and puts names/numbers in sep lists
  names = []
  numbers = []

  for i in range(len(dataSet)):
    if dataSet.iat[i, 1] in names:
      index = names.index(dataSet.iat[i, 1])
      numbers[index] += dataSet.iat[i, 2]
    else:
      names.append(dataSet.iat[i, 1])
      numbers.append(dataSet.iat[i, 2])

  #new dataframe with the updated info
  df_most_popular_all_time = pd.DataFrame({'Names': names, 'Number': numbers})

  #Sorts dataframe by count in descending order
  df_most_popular_all_time = df_most_popular_all_time.sort_values(
    by='Number', ascending=False)

  ranks = range(1,len(names) + 1)

  df_most_popular_all_time['Rank'] = ranks

  x = -1

  while(x == -1):
    print("Enter an x value: ",end = "")

    try:
      x = int(input())
    except:
      print("Invalid Input")
    else:

      if x > len(names) or x < 0:
        print("Invalid x Value (Out of Range)")
        x = -1

      else:
        print("\n" + df_most_popular_all_time.head(x).to_string(index = False))
