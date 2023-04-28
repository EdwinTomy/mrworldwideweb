from owlready2 import *
from owlready2 import sync_reasoner
from rdflib.plugins.sparql import prepareQuery
import numpy as np
from sklearn.linear_model import LinearRegression


# Mr.World Wide Web Project
# Web-based data integration
# @author Edwin Tomy George, Susana Perez, David Medina
# @version 1.0
# Description: The purpose of this project is to ready OWL ontologies and relate them with our topic
#              to answer questions relating to Weather and Car Accidents.
# Resources: https://pypi.org/project/Owlready2/ -- Owlready2
# Documentation to Owlready2: https://readthedocs.org/projects/owlready2/downloads/pdf/latest/


def query1(location):
    # Loading our ontology
    onto_path.append("/Users/edwintomy/PycharmProjects/mrworldwideweb/")
    onto = get_ontology("onto.owl").load()

    first_query = list(default_world.sparql("""
                   SELECT ?month (SUM(?elec) AS ?totalElec) (COUNT(?acc) AS ?numAcc) WHERE
                   {?date rdf:type onto:Date.
                    ?date onto:hasMonth ?month.
                    ?date onto:hasLocation ?loc.
                    ?loc onto:hasElectricCompany ?comp.
                    ?loc onto:hasName ??1.
                    ?comp onto:producesElectricOutput ?elec.
                    ?loc onto:hasAccident ?acc.} GROUP BY ?date
            """, [location]))
    return first_query

def answer1(location):
    query = query1(location)
    model = LinearRegression()
    model.fit([[i] for i in query[:][2]], query[:][1])
    print(model.coef_)
    return model.coef_[0]


def main():
    # Loading our ontology
    onto_path.append("/Users/edwintomy/PycharmProjects/mrworldwideweb/")
    onto = get_ontology("onto.owl").load()

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
    #main()
    answer1('El_Paso')
