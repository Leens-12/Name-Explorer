#!/usr/bin/env python3

# Libraries
import os
import sys
import getopt
import csv
import pandas as pd
from pathlib import Path

def main ( argv ):
  
  if len(argv) < 5:
    print ( "Invalid Call -> ./FileReadPrograms/readNewZealand.py -i <input file name> -f <output file name female> -m <output file name male>" )
    sys.exit(2)
    
  try:
    (opts, args) = getopt.getopt ( argv,"i:f:m:",["input=", "female=", "male="] )
      
  except getopt.GetoptError:
    print (  "Invalid Call -> ./FileReadPrograms/readNewZealand.py -i <input file name> -f <output file name female> -m <output file name male>" )
    sys.exit(2)
      
  for opt, arg in opts:
    if opt in ( "-i", "--input"):
      inputFileName = arg
    elif opt in ("-f", "--outputFemale"):
      outputFileNameFemale = arg
    elif opt in ("-m", "--outputMale"):
      outputFileNameMale = arg

  inputFilePath = "SourceCSVFiles/" + inputFileName + ".csv"
  outputFilePathFemale = "FormattedCSVFiles/" + outputFileNameFemale + ".csv"
  outputFilePathMale = "FormattedCSVFiles/" + outputFileNameMale + ".csv"
  

  inputPath = Path(inputFilePath)

  if inputPath.is_file() == False:
    print("Invalid Input File")
    sys.exit(2)
    
  year     = []
  names    = []
  number  = []
  total    = 0


  #read in male names
  #Year, Gender, Name, Count
  with open ( inputFilePath, encoding="utf8", errors="ignore"  ) as csvDataFile:
    next ( csvDataFile ) 
    csvReader = csv.reader(csvDataFile, delimiter=',')
    
    for row in csvReader:
      if int(row[0]) >= 1990 and int(row[0]) <= 2021 and row[1] == "M":
        year.append(int(row[0]))
        names.append(row[2])
        number.append(int(row[3]))
        total = total + 1

  #data into a dataFrame 
  maleNames = {'Year': year, 'Names': names, 'Number': number}
  maleNames_df = pd.DataFrame(maleNames)
  
  maleNames_df.sort_values(['Year', 'Number', 'Names'], axis = 0,
                          ascending = [False,False, True], 
                          inplace = True)

  currentYear = 0
  lastRank = 1
  rankCount = 1
  ranks = []

  #for all rows
  for i in range(total):
    #if year on row 'i' is different then var "currentYear", start rank at 1, change year
    if currentYear != int(maleNames_df.iat[i,0]):
      currentYear = int(maleNames_df.iat[i,0])
      rankCount = 1
      lastRank = 1

    #check if there is a previous entry from current year to compare
    if rankCount >= 2:
      #If current names popularity, set rank of current name to previous names rank
      if int(maleNames_df.iat[i-1, 2]) == int(maleNames_df.iat[i,2]):
        ranks.append(lastRank)

      #If previous "if" statement has not been met, carry out below
      else:
        ranks.append(rankCount)

    #assign ranks normally
    else:
      ranks.append(rankCount)

    #add to current rank, set lastRank to current rank that was assigned
    rankCount = rankCount + 1
    lastRank = ranks[i]

  #add rank column to data frame
  maleNames_df["Rank"] = ranks

  maleNames_df.to_csv(outputFilePathMale, sep = ",", index = False, encoding = 'utf-8')

  year.clear()
  names.clear()
  number.clear()
  ranks.clear()
  total = 0

  #read in female names
  #Year, Gender, Name, Count
  with open ( inputFilePath, encoding="utf8", errors="ignore"  ) as csvDataFile:
    next ( csvDataFile ) 
    csvReader = csv.reader(csvDataFile, delimiter=',')
    
    for row in csvReader:
      if int(row[0]) >= 1990 and int(row[0]) <= 2021 and row[1] == "F":
        year.append(int(row[0]))
        names.append(row[2])
        number.append(int(row[3]))
        total = total + 1

  #data into a dataFrame 
  femaleNames = {'Year': year, 'Names': names, 'Number': number}
  femaleNames_df = pd.DataFrame(femaleNames)
  
  femaleNames_df.sort_values(['Year', 'Number', 'Names'], axis = 0,
                          ascending = [False,False, True], 
                          inplace = True)

  currentYear = 0
  lastRank = 1
  rankCount = 1
  ranks = []

  #for all rows
  for i in range(total):
    #if year on row 'i' is different then var "currentYear", start rank at 1, change year
    if currentYear != int(femaleNames_df.iat[i,0]):
      currentYear = int(femaleNames_df.iat[i,0])
      rankCount = 1
      lastRank = 1

    #check if there is a previous entry from current year to compare
    if rankCount >= 2:
      #If current names popularity, set rank of current name to previous names rank
      if int(femaleNames_df.iat[i-1, 2]) == int(femaleNames_df.iat[i,2]):
        ranks.append(lastRank)

      #If previous "if" statement has not been met, carry out below
      else:
        ranks.append(rankCount)

    #assign ranks normally
    else:
      ranks.append(rankCount)

    #add to current rank, set lastRank to current rank that was assigned
    rankCount = rankCount + 1
    lastRank = ranks[i]

  #add rank column to data frame
  femaleNames_df["Rank"] = ranks

  femaleNames_df.to_csv(outputFilePathFemale, sep = ",", index = False, encoding = 'utf-8')
  
  
if __name__ == "__main__":
  main ( sys.argv[1:] )