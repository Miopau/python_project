#!/usr/bin/env python
import csv

class Installation:
    nom_installation = ""
    installation_id = 0
    nom_commune = ""
    code_postale = ""


    def __init__(self, nom_installation, installation_id, nom_commune, code_postale):
        self.nom_installation = nom_installation
        self.installation_id = installation_id
        self.nom_commune = nom_commune
        self.code_postale = code_postale

installationList = []

def readCSV():
    with open("../initial/installations.csv","r") as file:
        reader = csv.reader(file)
        for row in reader:
            installationList.append(installation(row[0],row[1],row[2],row[3]));
        for elt in installationList:
            elt.toString();
