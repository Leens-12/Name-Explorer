#!/usr/bin/env python3

#Read in formatted files, returns dataframe

import pandas as pd
from pathlib import Path
import csv

def readIn(fileName):
  filePath = "FormattedCSVFiles/" + fileName + ".csv"

  file_path = Path(filePath)
  if file_path.is_file() == False:
    print(fileName + ".csv was not found in FormattedCSVFiles folder.")
    return 0

  #declare variables to read file values into
  years = []
  names = []
  numbers = []
  ranks = []

  #open file
  with open(filePath, encoding="utf8", errors="ignore") as csvDataFile:
    next(csvDataFile)
    csvReader = csv.reader(csvDataFile, delimiter = ',')

    #read in each value on file
    for row in csvReader:
      years.append(int(row[0]))
      names.append(row[1])
      numbers.append(int(row[2]))
      ranks.append(int(row[3]))
      
  
  fullFile = {'Year': years, 'Name': names, 'Number': numbers, 'Rank': ranks}
  fullFile_df = pd.DataFrame(fullFile)

  return fullFile_df
  
