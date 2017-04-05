#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

class Equipement:
    installation_id = 0
    equipement_id = 0
    nom_equipement = ""

    def __init__(self, installation_id, equipement_id, nom_equipement):
        self.installation_id = installation_id
        self.equipement_id = equipement_id
        self.nom_equipement = nom_equipement

equipementList = []

def readCSV():
    with open("../initial/equipements.csv","r") as file:
        reader = csv.reader(file)
        for row in reader:
            equipementList.append(equipementList(row[2],row[4],row[5]));
        for elt in equipementList:
            elt.toString();
