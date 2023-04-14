from owlready2 import *
from owlready2 import sync_reasoner


# Mr.World Wide Web Project
# Web-based data integration
# @author Edwin Tomy George, Susana Perez, David Medina
# @version 1.0
# Description: The purpose of this project is to ready OWL ontologies and relate them with our topic
#              to answer questions relating to Weather and Car Accidents.
# Resources: https://pypi.org/project/Owlready2/ -- Owlready2
# Documentation to Owlready2: https://readthedocs.org/projects/owlready2/downloads/pdf/latest/


# Loading our ontology
onto_path.append("/Users/edwintomy/PycharmProjects/mrworldwideweb/")
onto = get_ontology("onto.owl").load()
# sync_reasoner(onto)

print("*** ONTOLOGY INFORMATION ***")
# Printing basic information of our ontology
print("These are our classes:", str(list(onto.classes())))
print("These are our individuals:", str(list(onto.individuals())))
print("These are our object properties:", str(list(onto.object_properties())))
print("These are our data properties:", str(list(onto.data_properties())))
print("******************************")


print("\n*** SIMPLE QUERIES TO ONTOLOGY ***")
print("QUERY #1 - Searching for individuals that are related to another one with the 'has_location' relation: "
      + str(list(onto.search(hasLocation="*"))))
print("QUERY #2 - Searching for individuals that are related to another one with the 'hasWeather' relation: "
      + str(list(onto.search(hasWeather="*"))))
print("QUERY #3 - Searching for individuals that are related to another one with the 'hasAccident' relation: "
      + str(list(onto.search(hasAccident="*"))))
print("QUERY #4 - Searching for individuals that are related to another one with the 'hasElectricCompany' relation: "
      + str(list(onto.search(hasElectricCompany="*"))))
print("QUERY #5 - Searching for entities that end with the iri 'Weather': " + str(list(onto.search(iri="*Weather"))))
print("QUERY #6 - Searching for individuals and subclasses of 'FatalAccident': "
      + str(list(onto.search(is_a=onto.FatalAccident))))
print("******************************")

print("DL QUERIES")
