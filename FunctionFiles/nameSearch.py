#Searches a given name from all datasets and outputs the rank/popularity of that name in each year

import matplotlib.pyplot as plt

#sends in a dataframe and a name
def nameSearch(dataSet, name):
  allOfName = dataSet[dataSet["Name"] == name ]

  #check if the name was found in the dataset
  #if not print this message
  if(allOfName.empty):
    print("The name " + name + " was not found in the dataset.\n")
  
  #otherwise continue
  else:
    total = 0

    #total all ranks of the name
    for i in range(len(allOfName)):
      total += allOfName.iat[i,3]

    #calculate the average rank
    averageRank = round(total / len(allOfName))
    
    print("Found the name " + name + " in the dataset, average rank was " + str(averageRank) + ".\n")

    userIn = -1
    
    while userIn != 0:
      print("-----Welcome to Name Search-----\n")
      print("Please Enter an option:\n1. Show Rank in a Year\n2. Print All Data\n3. Generate Graph")
      print("\nEnter your selection (0 to exit): ", end = "")

      try:
        userIn = int(input())
      except:
        print("\nInvalid Input\n")

      else:
        if userIn == 1:

          searchYear = 0

          #prompt user to enter a valid year
          while searchYear == 0 or searchYear < 1990 or searchYear > 2021:
            print("\nEnter a year (1990 - 2021): ", end = "")

            try:
              searchYear = int(input())

            except:
              print("\nInvalid Input\n")

            else:
              if searchYear < 1990 or searchYear > 2021:
                print("\nInvalid Input (Years 1990 - 2021 only)\n")

          printedOutput = False
          
          #print data based on year
          for i in range(len(allOfName)):
            if allOfName.iat[i,0] == searchYear:
              print("\nThe name " + name + " was rank " + str(allOfName.iat[i,3]) + " and used " + str(allOfName.iat[i,2]) + " time(s) in " + str(searchYear) +".\n")
              printedOutput = True

          #if nothing was printed then the name did not appear in that year
          #indicate this to user with this message
          if printedOutput == False:
            print("\nName not found in the year " + str(searchYear) + "\n")

        elif userIn == 2:
          print("\n" + allOfName.to_string(index = False) + "\n")
        
        elif userIn == 3:
          confirm = 0

          #prompt user for graph filename
          while confirm != 1:
            print("\nSave graph under what filename?")
            print("Enter name here (no special characters): ", end = "")
            graphNameBase = input()
            print("\nChosen filename: " + graphNameBase)
            print("Enter 1 to confirm")
            try:
              confirm = int(input())
            except:
              print("Invalid Input\n")

          #generate and save graph    
          allOfName.plot(x ='Year', y='Number', kind='line', legend = None)
          plt.title("Popularity of the Name " + name + " Over Time")
          plt.savefig('OutputGraphs/' + graphNameBase + '.png')
          print("Graph succesfully saved under name " + graphNameBase + ".png in OutputGraphs")
          