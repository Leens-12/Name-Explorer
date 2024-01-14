#!/usr/bin/env python3

import sys
import pandas as pd
from names_dataset import NameDataset

#nd = NameDataset()

#import all functions files
sys.path.append("FunctionFiles")
from mostPopularAllTime import mostPopularAllTime
#from mostPopularName import mostPopularName
from nameSearch import nameSearch
from nameEthnicity import nameEthnicity

sys.path.pop()
sys.path.append("FileReadPrograms")
from formattedReadIn import readIn

irelandMale = readIn("IrelandMaleName")
irelandFemale = readIn("IrelandFemaleName")

allData = []
compare = 0
nd = NameDataset()

if (type(irelandMale) != type(compare)):
  allData.append(irelandMale)

if (type(irelandFemale) != type(compare)):
  allData.append(irelandFemale)

print("Enter a program to test:")
print("2.mostPopularAllTime\n3.mostPopularName\n4.nameSearch\n5.nameEthnicity\n")

choice = int(input())


if choice == 2:
  mostPopularAllTime(irelandMale)
elif choice == 3:
  #mostPopularName(irelandMale, 2020)
  print("This function is currently broken")
elif choice == 4:
  nameSearch(irelandMale,"Jack")
elif choice == 5:
  nameEthnicity(irelandMale, nd)

