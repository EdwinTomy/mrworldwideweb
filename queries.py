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
    print("These are our individuals:", list(onto.individuals()))
    print("These are our object properties:", list(onto.object_properties()))
    print("These are our data properties:", list(onto.data_properties()))

    first_query = list(default_world.sparql("""
               SELECT (SUM(?elec) AS ?totalElec) (COUNT(?acc) AS ?numAcc) WHERE
               {?date rdf:type onto:Date.
                ?date onto:hasMonth ?month.
                ?date onto:hasLocation ?loc.
                ?loc onto:hasElectricCompany ?comp.
                ?comp onto:producesElectricOutput ?elec.
                ?loc onto:hasAccident ?acc.} GROUP BY ?date
        """))
    print(first_query)

    second_query = list(default_world.sparql("""
                   SELECT (AVG(?precip) AS ?avgPrecip) (COUNT(?acc) AS ?numAcc) WHERE
                   {?date rdf:type onto:Date.
                    ?date onto:hasMonth ?month.
                    ?date onto:hasLocation ?loc.
                    ?loc onto:hasWeather ?weather.
                    ?weather onto:hasPrecipitation ?precip.
                    ?loc onto:hasAccident ?acc.} GROUP BY ?date
            """))
    print(second_query)

    third_query = list(default_world.sparql("""
               SELECT (SUM(?elec) AS ?totalElec) (COUNT(?acc) AS ?numAcc) (AVG(?precip) AS ?extremeWeather)
               WHERE
               {?date rdf:type onto:Date.
                ?date onto:hasMonth ?month.
                ?date onto:hasLocation ?loc.
                ?loc onto:hasElectricCompany ?comp.
                ?comp onto:producesElectricOutput ?elec.
                ?loc onto:hasWeather ?weather.
                ?weather onto:hasPrecipitation ?precip.
                ?loc onto:hasAccident ?acc.} GROUP BY ?date
        """))
    print(third_query)


if __name__ == '__main__':
    main()
