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

def weather_dataset(onto, df):
    for index, row in df.iterrows():
        year_str, month_str, day_str = row['datetime'].split('-')
        date_str = str(int(year_str)) + '-' + str(int(month_str))
        date = onto.Date(date_str)
        date.hasMonth = int(month_str)
        date.hasYear = int(year_str)

        location_str = row['name'].replace(' ', '_') + '-' + date_str
        location = onto.Location(location_str)
        weather_str = location_str + '-' + day_str

        if row['tempmin'] < 0 or row['tempmax'] > 35 or row['precip'] > 10 or row['visibility'] < 5 or row['windspeed'] > 20:
            weather = onto.ExtremeWeather(weather_str)
        else:
            weather = onto.NonExtremeWeather(weather_str)

        weather.hasMinTemp = row['tempmin']
        weather.hasMaxTemp = row['tempmax']
        weather.hasMeanTemp = row['temp']
        weather.hasPrecipitation = row['precip']
        weather.hasVisibility = row['windspeed']
        weather.hasWindSpeed = row['visibility']

        date.hasLocation.append(location)
        location.hasWeather.append(weather)
        location.hasName = row['name'].replace(' ', '_')


def weather_datasets():
    onto_path.append("/Users/edwintomy/PycharmProjects/mrworldwideweb/")
    onto = get_ontology("onto.owl").load()

    df_au = pd.read_csv('data/austin_weather.csv')
    df_da_ho = pd.read_csv('data/dallas_houston_weather.csv')
    df_ep_sa = pd.read_csv('data/elpaso_sanantonio_weather.csv')

    weather_dataset(onto, df_au)
    weather_dataset(onto, df_da_ho)
    weather_dataset(onto, df_ep_sa)

    onto.save()


def electricity_datasets():
    # Loading our ontology
    onto_path.append("/Users/edwintomy/PycharmProjects/mrworldwideweb/")
    onto = get_ontology("onto.owl").load()

    df = pd.read_excel('data/net_metering2019.xlsx')

    company_to_location = {'El Paso Electric Co': 'El_Paso',
                           'City of San Antonio - (TX)': 'Both',
                           'Entergy Texas Inc.': 'Houston',
                           'Adjustment 2019': 'Dallas',}

    for index, row in df.iterrows():
        company_name = row['Utility Name']
        date_name = str(row['Year']) + '-' + str(int(row['Month']))
        if row['State'] != 'TX':
            continue
        location_name = company_to_location[company_name]

        if location_name == 'Both':
            full_company_name0 = company_name + date_name + '0'
            full_company_name1 = company_name + date_name + '1'
            company0 = onto.CityElectricCompany(full_company_name0)
            company1 = onto.CityElectricCompany(full_company_name1)
            location0 = onto.Location('{}-'.format('Austin') + date_name)
            location1 = onto.Location('{}-'.format('San_Antonio') + date_name)
            location0.hasElectricCompany = company0
            location1.hasElectricCompany = company1
            company0.producesElectricOutput = row['Total'] / 2
            company1.producesElectricOutput = row['Total'] / 2

        else:
            full_company_name0 = company_name + date_name
            company0 = onto.CityElectricCompany(full_company_name0)
            location0 = onto.Location('{}-'.format(location_name) + date_name)
            location0.hasElectricCompany = company0
            company0.producesElectricOutput = row['Total']

    onto.save()



if __name__ == '__main__':
    weather_datasets()
    electricity_datasets()
