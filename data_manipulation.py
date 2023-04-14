import csv
from owlready2 import *

onto_path.append("/Users/edwintomy/PycharmProjects/mrworldwideweb/")
onto = get_ontology("onto.owl").load()

class Accident(Thing):
    namespace = onto

    def __init__(self, date=None,):
        super().__init__()
        self.date = None
        self.fatalAccident = None
        self.driverAlcoholResult = None


# Read the data from the CSV file
with open("Users/edwintomy/PycharmProjects/mrworldwideweb/austinAccidents.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Create a new instance of Person for each row
        date = Date(name=row[])

        # Add the instance to the ontology
        onto.add(person)

# Save the ontology
onto.save(file="path/to/save/ontology.owl")
