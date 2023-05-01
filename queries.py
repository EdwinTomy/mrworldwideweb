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
    return model.coef_[0]


def query2(location):
    # Loading our ontology
    onto_path.append("/Users/edwintomy/PycharmProjects/mrworldwideweb/")
    onto = get_ontology("onto.owl").load()

    second_query = list(default_world.sparql("""
                       SELECT ?month (AVG(?precip) AS ?avgPrecip) (COUNT(?acc) AS ?numAcc) WHERE
                       {?date rdf:type onto:Date.
                        ?date onto:hasMonth ?month.
                        ?date onto:hasLocation ?loc.
                        ?loc onto:hasWeather ?weather.
                        ?loc onto:hasName ??1.
                        ?weather onto:hasPrecipitation ?precip.
                        ?loc onto:hasAccident ?acc.} GROUP BY ?date
                """, [location]))
    return second_query


def answer2(location):
    query = query2(location)

    sorted_query = sorted(query, key=lambda x: x[2], reverse=True)
    sorted_query_rain = sorted(query, key=lambda x: x[1], reverse=True)

    pos = 1
    for i in range(len(sorted_query_rain)):
        if sorted_query_rain[i][0] == sorted_query[0][0]:
            break

    return sorted_query[0][0], sorted_query[0][1], pos


def query3(location):
    # Loading our ontology
    onto_path.append("/Users/edwintomy/PycharmProjects/mrworldwideweb/")
    onto = get_ontology("onto.owl").load()

    third_query0 = list(default_world.sparql("""
               SELECT (COUNT(DISTINCT ?weather) AS ?total) (SUM(?elec) AS ?totalElec) (COUNT(?acc) AS ?numAcc) 
               WHERE
               {?date rdf:type onto:Date.
                ?date onto:hasMonth ?month.
                ?date onto:hasLocation ?loc.
                ?loc onto:hasName ??1.
                ?loc onto:hasElectricCompany ?comp.
                ?comp onto:producesElectricOutput ?elec.
                ?loc onto:hasWeather ?weather.
                ?weather rdf:type onto:ExtremeWeather.
                ?loc onto:hasAccident ?acc.} 
        """, [location]))

    third_query1 = list(default_world.sparql("""
               SELECT (COUNT(DISTINCT ?weather) AS ?total) (SUM(?elec) AS ?totalElec) (COUNT(?acc) AS ?numAcc) 
               WHERE
               {?date rdf:type onto:Date.
                ?date onto:hasMonth ?month.
                ?date onto:hasLocation ?loc.
                ?loc onto:hasName ??1.
                ?loc onto:hasElectricCompany ?comp.
                ?comp onto:producesElectricOutput ?elec.
                ?loc onto:hasWeather ?weather.
                ?weather rdf:type onto:NonExtremeWeather.
                ?loc onto:hasAccident ?acc.} 
        """, [location]))

    return [["Extreme Weather", third_query0[0][2] / third_query0[0][0], third_query0[0][1] / third_query0[0][0]],
            ["NonExtreme Weather", third_query1[0][2] / third_query1[0][0], third_query1[0][1] / third_query1[0][0]]]


def answer3(location):
    q = query3(location)
    return q[0][2]/q[1][2], q[0][1]/q[1][1], q[0][2]/q[1][2] / (q[0][1]/q[1][1])




if __name__ == '__main__':
    names = ['El_Paso', 'Austin', 'Houston', 'Dallas', 'San_Antonio']
    for name in names:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(name)
        print(query1(name))
        print(answer1(name))
        print(query2(name))
        print(answer2(name))
        print(query3(name))
        print(answer3(name))

