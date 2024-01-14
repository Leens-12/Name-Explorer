
#import libraries
import sys
import pandas as pd
from names_dataset import NameDataset,NameWrapper

#import all functions files
sys.path.append("FunctionFiles")
from nameSearch import nameSearch
from nameEthnicity import nameEthnicity
from mostPopularAllTime import mostPopularAllTime
sys.path.pop()
sys.path.append("FileReadPrograms")
from formattedReadIn import readIn

print("\nLoading Files and Libraries Please Wait\n")

#Load name ethnicity dataset (takes a while)(note does not run on replit, takes too much RAM space)
#if running on replit comment this line out, name1
#Ethnicity will only work on machines with 3gb of RAM
nd = NameDataset()

#read in all formatted files
irelandMale = readIn("IrelandMaleName")
irelandFemale = readIn("IrelandFemaleName")
australiaMale = readIn("AustraliaMaleName")
australiaFemale = readIn("AustraliaFemaleName")
newZealandMale = readIn("NewZealandMaleName")
newZealandFemale = readIn("NewZealandFemaleName")

#runFunction takes in a dataSet, checks if it's valid then prompts the user to
#choose what function to run
def runFunction (dataSet):

  userFuncChoice = -1

  if type(0) == type(dataSet):
    print("\nError: File Was Not Found")
    return 0
  
  else:
    print("\nFile Was Found\n")

    while userFuncChoice != 0:
      print("Please Select a Function:")
      print("1. Search for a Name")
      print("2. Check Name Ethnicity")
      print("3. Print Top X Names of All Time")
      print("\nEnter your selection (0 to exit): ", end = "")
      try:
        userFuncChoice = int(input())
      except:
        print("\nInvalid Input\n")
      else:

        if userFuncChoice > 3 or userFuncChoice < 0:
          print("\nInvalid Input\n")

        elif userFuncChoice == 1:
          print("Enter a name to search for: ", end = "")
          name = input().title()
          print()
          nameSearch(dataSet,name)
          break

        elif userFuncChoice == 2:
          nameEthnicity(dataSet, nd) #comment out on replit, add a print
          break

        elif userFuncChoice == 3:
          mostPopularAllTime(dataSet)
          break
    
userFileChoice = -1

#main loop prompts user to pick a file, then runs runFunction
while(userFileChoice != 0):
  print("\n-----Welcome to Name Explorer-----")
  print("\nPlease Choose a File:")
  print("1. Ireland Male Names")
  print("2. Ireland Female Names")
  print("3. Australia Male Names")
  print("4. Australia Female Names")
  print("5. New Zealand Male Names")
  print("6. New Zealand Female Names")
  print("\nEnter your selection (0 to exit): ", end="")
  
  try:
    userFileChoice = int(input())
  except:
    print("\nInvalid Input\n")
  else:
    if userFileChoice > 6 or userFileChoice < 0:
      print("\nInvalid Input\n")
    elif userFileChoice == 1:
      runFunction(irelandMale)
    elif userFileChoice == 2:
      runFunction(irelandFemale)
    elif userFileChoice == 3:
      runFunction(australiaMale)
    elif userFileChoice == 4:
      runFunction(australiaFemale)
    elif userFileChoice == 5:
      runFunction(newZealandMale)
    elif userFileChoice == 6:
      runFunction(newZealandFemale)
