import csv
from owlready2 import *

onto_path.append("C:/Users/susan/Downloads/mrworldwideweb/onto.owl")
onto = get_ontology("onto.owl").load()

class Accident(Thing):
    namespace = onto
    def __init__(self, crashID, personAge):
        self.crashID = crashID
        self.personAge = personAge

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


# Read the data from the CSV file
# with open("C:/Users/susan/Downloads/mrworldwideweb/accidents_austin.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         # Create a new instance of Accident for each row
#         print(row['Crash ID'])
#         #accident = Accident(crashID=row['crashID'])
#         # Add the instance to the ontology
#         #onto.add(accident)
with open("C:/Users/susan/Downloads/mrworldwideweb/accidents_austin.csv", "r", encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    # Print the header row
    print(reader.fieldnames)
    d = {}

    # #possible approach: create a dict-> id:Accident and then traverse dictionary to add to ontology
    # for row in reader:
    #     # Create a new instance of Accident for each row
    #     #print(row['Person Age'], row['Person Death Count'], row['Person Total Injury Count'])
    #     #accident = Accident(crashID=row['ï»¿"Crash ID"'], personAge=row["Person Age"])
    #     #accident.personAge = row['Person Age']
    #     #onto.add(accident)
    #     crashID = row['Crash ID']
    #     if crashID not in d:
    #         d[crashID] = 1
    #     else:
    #         d[crashID] +=1
            
    # print(d)



# Save the ontology
#onto.save(file="path/to/save/ontology-test.owl")
