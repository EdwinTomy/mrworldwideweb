from owlready2 import *
from owlready2 import sync_reasoner
from rdflib.plugins.sparql import prepareQuery


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
    # print("These are our individuals:", list(onto.individuals()))
    # print("These are our object properties:", list(onto.object_properties()))
    # print("These are our data properties:", list(onto.data_properties()))

    #query = prepareQuery('SELECT ?x WHERE { ?x rdf:type onto.Location }',
    #                     initNs={"onto": onto.base_iri})
    #result = onto.search(query)
    #for row in result:
    #    print(row["x"])

    list(default_world.sparql("""
               SELECT (COUNT(?x) AS ?nb)
               { ?x a owl:Class . }
        """))

    # ****** PERFORMING SIMPLE QUERIES: ******

    # Searching individuals of a given class
    # onto.search(type="Date")

    # Searching entities by its full IRI
    # onto.search(iri="*")

    # Searching subclasses of a given class
    # onto.search(subclass_of="*Accident")
    #
    # Searching both individuals and subclasses of a given class
    # onto.search(subproperty_of="*Accident")

    # ****************************************


if __name__ == '__main__':
    main()
