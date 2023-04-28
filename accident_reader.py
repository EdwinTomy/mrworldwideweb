from owlready2 import *
from owlready2 import sync_reasoner
from rdflib.plugins.sparql import prepareQuery
import pandas as pd


# Mr.World Wide Web Project
# Web-based data integration
# @author Edwin Tomy George, Susana Perez, David Medina
# @version 1.0
# Description: The purpose of this project is to ready OWL ontologies and relate them with our topic
#              to answer questions relating to Weather and Car Accidents.
# Resources: https://pypi.org/project/Owlready2/ -- Owlready2
# Documentation to Owlready2: https://readthedocs.org/projects/owlready2/downloads/pdf/latest/


def accident_dataset(df_name, name, onto):
    df = pd.read_csv(df_name)
    for index, row in df.iterrows():
        if index%20 != 0:
            continue
        accident_str = 'accident_' + str(row['CrashID'])
        #print(row['CrashID'])
        accident = onto.Accident(accident_str)
        accident.deathCount = row['CrashDeathCount']
        if row['PersonAlcoholResult'] == 'NoData':
            accident.driverAlcoholResult = True
        else:
            accident.driverAlcoholResult = True
        accident.personAge = row['PersonAge']

        location = onto.Location('{}-2019-'.format(name) + str(row['CrashMonth']))
        location.hasAccident.append(accident)


def accident_datasets():
    # Loading our ontology
    onto_path.append("/Users/edwintomy/PycharmProjects/mrworldwideweb/")
    onto = get_ontology("onto.owl").load()

    # Create an instance of the class

    accident_dataset('data/austin_accidents.csv', 'Austin', onto)
    accident_dataset('data/dallas_accidents.csv', 'Dallas', onto)
    accident_dataset('data/houston_accidents.csv', 'Houston', onto)
    accident_dataset('data/el_paso_accidents.csv', 'El_Paso', onto)
    accident_dataset('data/san_antonio_accidents.csv', 'San_Antonio', onto)

    onto.save()



if __name__ == '__main__':
    accident_datasets()
