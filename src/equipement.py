#!/usr/bin/env python
import csv

class Equipement:
    code_postale = 0
    nom_commune = ""
    installation_id = 0
    nom_installation = ""
    equipement_id = 0
    nom_equipement = ""

    def __init__(self, code_postale, nom_commune, installation_id, nom_installation, equipement_id, nom_equipement):
        self.code_postale = code_postale
        self.nom_commune = nom_commune
        self.installation_id = installation_id
        self.nom_installation = nom_installation
        self.equipement_id = equipement_id
        self.nom_equipement = nom_equipement

equipementList = []

def readCSV():
    with open("../initial/equipements.csv","r") as file:
        reader = csv.reader(file)
        for row in reader:
            equipementList.append(equipementList(row[0],row[1],row[2],row[3],row[4],row[5]));
        for elt in equipementList:
            elt.toString();
