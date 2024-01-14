# Name Explorer

## **Overview**
This program allows a user to analyze the formatted name data provided. Allows user to search for a name, and check for name ethnicities in a country.

## **Prerequisites:**
- Python 3 must be installed (install from python.org)
- 3.2 GB of RAM required for the library names_dataset
  
Required Libraries:
- pandas
- matplotlib
- names_dataset


**On Windows Only:**
- Run install.bat to install all libraries


**On Windows, Linux and Mac:**
- Install all libraries with: pip install -r requirements.txt


## **How To Run The Program:**

*Main:*

**On Windows Only:**
- Run run.bat (on Windows machines with Python and Libraries installed)


**On Windows Linux and Mac:**
- Open command prompt/terminal in the folder with main.py
- Then type "python.exe main.py" (Windows) or "python3 main.py" (Linux and Mac)


Programs in FileReadPrograms:
- Open command prompt/terminal in the folder with main.py


**Windows:**
- Run with "python.exe FileReadPrograms\nameOfFunc.py -i input ... (rest of commandline arguments)


**Linux/Mac:**
- Run with "python3 FileReadProgram/nameOfFunc.py -i input ... (rest of commandline arguments)



- Enter input and output file names on commandline as only their names (not a filepath or extension, i.e. to read in AustraliaNamesRaw.csv in SourceCSVFiles, enter AustraliaNamesRaw as input commandline arguement)


## **Notes:**
- names_dataset requires 3.2GB of RAM to load the name origin dataset
- names_dataset also takes some time to load when running main.py
- Any filenames should not contain any special characters (Windows throws an OS error when this happens)
- All graphs are output to the OutputGraphs file and are stored as a .png
- All source csv files are in SourceCSVFiles, and all formatted csv files are in FormattedCSVFiles
