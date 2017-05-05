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
