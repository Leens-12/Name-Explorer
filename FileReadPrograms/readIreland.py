#!/usr/bin/env python3

#Approx. Runtime: 7.76 seconds

import pandas as pd
import csv
import getopt
import sys
from pathlib import Path

def main( argv ):
  
  #check commandline arguments
  if len(argv) < 4:
    print("Invalid Call (./FileReadPrograms/readIreland.py -i <inputFilePath> -o <outputFilePath>)")
    sys.exit(2)

  try:
    (opts, args) = getopt.getopt(argv,"i:o:", ["input=", "output="])
  
  except getopt.GetoptError:
    print("Invalid Call (./FileReadPrograms/readIreland.py -i <inputFilePath> -o <outputFilePath>)")
    sys.exit(2)

  #parse commandline arguments
  for opt, arg in opts:
    if opt in ("-i", "--input"):
      inputFilePathBase = arg
    elif opt in ("-o", "--output"):
      outputFilePathBase = arg

  #assign correct filepath
  inputFilePath = "SourceCSVFiles/" + inputFilePathBase + ".csv"
  outputFilePath = "FormattedCSVFiles/" + outputFilePathBase + ".csv"

  inputPath = Path(inputFilePath)

  #Check that input file exists
  if inputPath.is_file() == False:
    print("Invalid Input File")
    sys.exit(2)

  #declare variables to read file values into
  years = []
  names = []
  numbers = []
  total = 0

  #open file
  with open(inputFilePath, encoding="utf8", errors="ignore") as csvDataFile:
    next(csvDataFile)
    csvReader = csv.reader(csvDataFile, delimiter = ',')

    #check each row that has a number given to it (no blanks in 4th column)
    #only read in years from 1990 - 2021 (check planning doc for more info)
    for row in csvReader:
      if row[3] != '' and int(row[0]) >= 1990 and int(row[0]) <= 2021:
        years.append(int(row[0]))
        names.append(row[1])
        numbers.append(int(row[3]))
        total = total + 1
        

  #put all data onto a dataframe and sort
  allNames = {'Year': years, 'Names': names, "Number": numbers}
  allNames_df = pd.DataFrame(allNames)

  allNames_df.sort_values(['Year', 'Number', 'Names'], axis = 0,
                          ascending = [False,False, True], 
                          inplace = True)


  currentYear = 0
  lastRank = 1
  rankCount = 1
  ranks = []

  #for all rows (int total)
  for i in range(total):
    #if the year is different than current year, start ranks from 1, change current year
    if currentYear != int(allNames_df.iat[i,0]):
      currentYear = int(allNames_df.iat[i,0])
      rankCount = 1
      lastRank = 1

    #Check if there is a previous entry from the current year to compare to
    if rankCount >= 2:
      #if popularity is the same, assign the current entry the rank of the previous
      if int(allNames_df.iat[i-1,2]) == int(allNames_df.iat[i,2]):
        ranks.append(lastRank)
        
      #otherwise assign rank normally
      else:
        ranks.append(rankCount)
        
    #assign ranks normally  
    else:
      ranks.append(rankCount)

    #increment current rank by one each iteration, set lastRank to the current rank that was assigned  
    rankCount = rankCount + 1
    lastRank = ranks[i]

  #add rank column to the dataframe
  allNames_df["Rank"] = ranks
    

  #export the dataframe to a csv file in the formatted folder
  allNames_df.to_csv(outputFilePath, sep = ",", index = False, encoding = 'utf-8')
  
if __name__ == "__main__":
    main ( sys.argv[1:] )