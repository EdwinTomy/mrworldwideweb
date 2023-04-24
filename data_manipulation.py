import csv
from owlready2 import *

onto_path.append("C:/Users/susan/Downloads/mrworldwideweb/onto.owl")
onto = get_ontology("onto.owl").load()

class Accident(Thing):
    namespace = onto
    def __init__(self, crashID, crashDeathCount, crashMonth, personAlcoholResult):
        #Crash ID,Crash Death Count,Crash Month,Latitude,Longitude,Person Age,Person Alcohol Result
        self.crashID = crashID
        self.crashDeathCount = crashDeathCount
        self.crashMonth = crashMonth
        self.personAge = []
        self.personAlcoholResult = personAlcoholResult       

class Location(Thing):
    namespace = onto
    def __init__(self):
        self.Weather = None
        self.cityElectricCompany = None
        self.latitude = None
        self.longitude = None

class Weather(Thing):
    namespace = onto
    def __init__(self):
        self.hasVisibility = None
        self.hasWindSpeed = None
        self.hasPrecipitation = None
        self.hasMaxTemp = None
        self.hasAverageTemp = None
        self.hasMinTemp = None

class Date(Thing):
    namespace = onto
    def __init__(self):
        self.month = None
        self.year = None 

class ElectricCompany(Thing):
    namespace = onto
    def __init__(self):
        self.producesElectricOutputOf = None


# Read the data from the CSV file
# with open("C:/Users/susan/Downloads/mrworldwideweb/accidents_austin.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         # Create a new instance of Accident for each row
#         print(row['Crash ID'])
#         #accident = Accident(crashID=row['crashID'])
#         # Add the instance to the ontology
#         #onto.add(accident)
onto = get_ontology("onto.owl").load()

with open("C:/Users/susan/Downloads/mrworldwideweb/AUSTIN.csv", "r", encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    # Print the header row
    print(reader.fieldnames)
    d = {}
    #THIS IS JUST ONE DRIVER PER ACCIDENT
    #personAge=row["Person Age"]
    #Crash ID,Crash Death Count,Crash Month,Latitude,Longitude,Person Age,Person Alcohol Result
    for row in reader:
        if row["Person Age"] not in d:
            accident = Accident(crashID=row["Crash ID"], crashDeathCount=row["Crash Death Count"], crashMonth=row["Crash Month"],personAlcoholResult=row["Person Alcohol Result"])
            accident.personAge.append(row["Person Age"])
            d[row["Crash ID"]] = accident
            onto.add(accident)
            onto.sync_reasoner()
        
    print(len(d))
# Save the ontology
onto.save(file="path/to/save/ontology-test.owl")
