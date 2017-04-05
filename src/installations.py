#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Importation of the csv library
import csv

class Installation:
    """
    Variable and class declaration
    """
    installationName = ""
    installation_id = 0
    cityName = ""
    zipCode = ""
    installationAdress =""
    longitude = 0
    latitude = 0
    disabledAdapted = False

    def __init__(self, installationName, installation_id, cityName, zipCode, installationAdress, longitude, latitude, disabledAdapted):
        """
        Construct function of the class
        """
        self.installationName = installationName
        self.installation_id = installation_id
        self.cityName = cityName
        self.zipCode = zipCode
        self.installationAdress = installationAdress
        self.longitude = longitude
        self.latitude = latitude
        self.disabledAdapted = disabledAdapted

    #Initialisation of the list
    installationList = []

    def readCSV():
        """
        Function that read the csv and create Equipment list
        """
        with open("../initial/installations.csv","r") as file:
            reader = csv.reader(file)
            for row in reader:
                installationList.append(installation(row[0],row[1],row[2],row[4],row[5]+" "+row[6],row[9],row[10], row[12]));
            return installationList #Return the list of installation
