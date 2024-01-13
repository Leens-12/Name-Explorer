#THIS FUNCTION WILL NOT RUN ON REPLIT
#Be sure to comment out any reference to it on main before running

from names_dataset import NameDataset,NameWrapper
import pandas as pd
import matplotlib.pyplot as plt

list_countries = ["Afghanistan", "Albania", "Algeria", "Angola", "Argentina", "Austria", "Azerbaijan", "Bahrain", "Bangladesh", "Belgium",
                  "Bolivia", "Botswana","Brazil", "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burundi", 
                  "Cambodia", "Cameroon", "Canada", "Chile", "China", "Colombia", "Costa Rica", "Croatia", "Cyprus", "Czechia", "Denmark", 
                  "Djibouti", "Ecuador", "Egypt", "El Salvador", "Estonia", "Ethiopia", "Fiji", "Finland", "France", "Georgia", "Germany",
                  "Ghana", "Greece", "Guatemala", "Haiti", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran", 
                  "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Korea", "Kuwait", "Lebanon", "Libya",
                  "Lithuania", "Luxembourg", "Macao", "Malaysia", "Maldives", "Malta", "Mauritius", "Mexico", "Moldova", "Morocco", 
                  "Namibia", "Netherlands", "Nigeria", "Norway", "Oman", "Palestine", "Panama", "Peru", "Philippines", "Poland", "Portugal", 
                  "Puerto Rico", "Qatar", "Russian Federation", "Saudi Arabia", "Serbia", "Singapore", "Slovenia", "South Africa", "Spain",
                  "Sudan", "Sweden", "Switzerland", "Syrian Arab Republic", "Taiwan", "Tunisia", "Turkey", "Turkmenistan", 
                  "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Yemen"]

#Generates graph and prints data based on given inputs
def displayData(data, xLabel, yLabel, graphType):
    userChoice = -1
    while(userChoice != 0):

        print("\nEnter an Option: ")
        print("1. Print Popularity Origin Data")
        print("2. Generate Graph")
        print("\nEnter here (0 to exit): ", end = "")

        try:
            userChoice = int(input())
        except:
            print("\nInvalid Input\n")
        else:
            if userChoice < 0 or userChoice > 2:
                print("\nInvalid Input\n")

            #the prints here are different as the data for the pie graphs are formatted slightly differently
            elif userChoice == 1:
                if(graphType == "line"):
                    print("\n" + data.to_string(index = False) + "\n")
                else:
                    print("\n" + data.to_string() + "\n")
    
            elif userChoice == 2:

                #plot graph and change label based on type of graph
                data.plot(x = xLabel, y = yLabel, kind = graphType, legend = None)
                if graphType == "pie":
                    plt.ylabel("")
                
                elif graphType == "line":
                    plt.ylabel("Popularity")

                confirm = 0

                #prompt user for both graph title and filename
                while(confirm != 1):
                    print("\nEnter the graph title: ", end = "")
                    graphTitle = input()
                    print("\nEnter filename to save graph under (no special characters or file extension): ", end = "")
                    graphFile = input()

                    #ask user to confirm their choices for title and filename
                    print("\nChosen Graph Title : " + graphTitle)
                    print("Chosen Graph Filename : " + graphFile +".png")
                    print("\nEnter 1 to confirm (0 to go back): ", end = "")

                    try:
                        confirm = int(input())
                    except:
                        print("\nInvalid Input")
                
                #save graph using title and filename
                plt.title(graphTitle)
                plt.savefig('OutputGraphs/' + graphFile + '.png')
                
                #indicate to user where the graph was saved to
                print("\nGraph saved in OutputGraphs under filename: " + graphFile + ".png")


def nameEthnicity(dataSet, nd):
    #Features in this
    #Origin of names all time (add all popularity totals per country) (generate pie graph with this info)
    #Origin of names in a certain year (add all popularity per country but in one year) (generate pie graph)
    #Line graph of a certain origin of names over the years (generate line graph)

    userChoice = -1

    while userChoice != 0:
        print("\n-----Welcome to Name Ethnicity-----\n")
        print("Please Enter an Option:")
        print("1. Overall Popularity of Each Name Origin")
        print("2. Popularity of Each Name Origin for a Year")
        print("3. Popularity of a Name Origin Over the Years")
        print("\nEnter your selection (0 to exit): ", end = "")

        origin = []
        number = []
        year = []
        givenYear = 0
        
        try:
            userChoice = int(input())
        except:
            print("\nInvalid Input\n")
        else:
            if userChoice < 0 or userChoice > 3:
                print("\nInvalid Input\n")

            #takes around 15 seconds to run on our machine
            elif userChoice == 1:
                print("\nLoading, Please Wait\n")
        
                for i in range(len(dataSet)):

                    #if country is already in the list of origins then just add the total to it's entry on the number list
                    if NameWrapper(nd.search(dataSet.iat[i,1])).country in origin and NameWrapper(nd.search(dataSet.iat[i,1])).country != "":
                        number[origin.index(NameWrapper(nd.search(dataSet.iat[i,1])).country)] += dataSet.iat[i,2]
                    
                    #otherwise make a new entry on the origin and number list
                    elif NameWrapper(nd.search(dataSet.iat[i,1])).country != "":
                        origin.append(NameWrapper(nd.search(dataSet.iat[i,1])).country)
                        number.append(dataSet.iat[i,2])
                
                #create dataframe then add all origins that have a total less than 10,000 into an other category
                #helps clean data output when printing and when making the graph (otherwise there would be over 20 entries on each pie graph)
                overallPop = {'Name Origin': origin, 'Number': number}
                overallPop_df = pd.DataFrame(overallPop)

                overallPop_df.loc[overallPop_df.Number < 10000, 'Name Origin'] = 'Other' 
                overallPop_df = overallPop_df.groupby('Name Origin').sum()
                overallPop_df.sort_values('Number',ascending=False, inplace=True)

                displayData(overallPop_df, "Name Origin", "Number", "pie")

            elif userChoice == 2:
                print("Enter a year (1990-2021): ", end = "")

                try:
                    givenYear = int(input())
                except:
                    print("\nInvalid Input\n")
                else:
                    if(givenYear > 2021 or givenYear < 1990):
                        print("\nInvalid Year (1990 - 2021 only)\n")
                    else:
                        #make a new dataset only containing entries from the year given
                        ethnicYear = dataSet[dataSet["Year"] == givenYear ]

                        for i in range(len(ethnicYear)):

                            #if country is already in the list of origins then add the total to it's corrosponding entry
                            if NameWrapper(nd.search(ethnicYear.iat[i,1])).country in origin and NameWrapper(nd.search(ethnicYear.iat[i,1])).country != "":
                                number[origin.index(NameWrapper(nd.search(ethnicYear.iat[i,1])).country)] += ethnicYear.iat[i,2]

                            #otherwise make a new entry for both origin and number
                            elif NameWrapper(nd.search(ethnicYear.iat[i,1])).country != "":
                                origin.append(NameWrapper(nd.search(ethnicYear.iat[i,1])).country)
                                number.append(ethnicYear.iat[i,2])
                        
                        #create dataframe and group all origins that have a total less than 200 into other
                        #helps clean data output when printing and for the graph
                        yearPop = {'Name Origin': origin, 'Number': number}
                        yearPop_df = pd.DataFrame(yearPop)

                        yearPop_df.loc[yearPop_df.Number < 200, 'Name Origin'] = 'Other' 
                        yearPop_df = yearPop_df.groupby('Name Origin').sum()
                        yearPop_df.sort_values('Number',ascending=False, inplace=True)

                        displayData(yearPop_df, "Name Origin", "Number", "pie")

            elif userChoice == 3:
                print("Enter a Country of origin to track: ", end = "")
                ethnicSearch = input().title()

                #check if given country is in the dataset's list of countries
                if ethnicSearch in list_countries:

                    for i in range(len(dataSet)):

                        #when a name with a matching country of origin is found, add it to the total for that year
                        if NameWrapper(nd.search(dataSet.iat[i,1])).country == ethnicSearch:

                            #if the year already has an entry just add to it
                            if dataSet.iat[i,0] in year:
                                number[year.index(dataSet.iat[i,0])] += dataSet.iat[i,2]

                            #otherwise make a new entry for that year in both lists
                            else:
                                year.append(dataSet.iat[i,0])
                                number.append(dataSet.iat[i,2])

                    #if no years are read in, print that no names from that country was found
                    if len(year) == 0:
                        print("\nNo names from " + ethnicSearch + " in this country.")
                    
                    #otherwise create and sort the dataframe
                    else:
                        ethnicData = {"Year": year, "Number": number}
                        ethnicData_df = pd.DataFrame(ethnicData)
                        ethnicData_df.sort_values('Year',ascending=True, inplace=True)
                        displayData(ethnicData_df, "Year", "Number", "line")
                
                #if the entered country is not valid print message to user
                else:
                    print("\nNot a valid country in the database")
                    
