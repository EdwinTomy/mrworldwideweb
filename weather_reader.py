from owlready2 import *
from owlready2 import sync_reasoner
from rdflib.plugins.sparql import prepareQuery
import pandas as pd
import json


# Mr.World Wide Web Project
# Web-based data integration
# @author Edwin Tomy George, Susana Perez, David Medina
# @version 1.0
# Description: The purpose of this project is to ready OWL ontologies and relate them with our topic
#              to answer questions relating to Weather and Car Accidents.
# Resources: https://pypi.org/project/Owlready2/ -- Owlready2
# Documentation to Owlready2: https://readthedocs.org/projects/owlready2/downloads/pdf/latest/



def main():
    # Loading our ontology
    onto_path.append("/Users/edwintomy/PycharmProjects/mrworldwideweb/")
    onto = get_ontology("onto.owl").load()

    #sync_reasoner(onto)

    # Printing basic information of our ontology
    print("These are our classes:", list(onto.classes()))
    print("These are our individuals:", list(onto.individuals()))
    print("These are our object properties:", list(onto.object_properties()))
    print("These are our data properties:", list(onto.data_properties()))

    # Create an instance of the class

    data = json.load(open('austin.json'))

    df = pd.DataFrame(data)
    for index, row in df.iterrows():
        name = 'accident_' + str(row['Crash ID'])
        accident = onto.Accident(name)

        print(df.head())

        accident.deathCount = row['Death Count']
        if row['Person Alcohol Result'] == 'No Data':
            accident.driverAlcoholResult = True
        else:
            accident.driverAlcoholResult = True
        accident.personAge = row['Person Age']


    print("These are our individuals:", list(onto.individuals()))
    onto.save()





if __name__ == '__main__':
    main()
