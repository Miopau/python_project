#!/usr/bin/env python
import csv

class Activite:
    code_postale = 0
    nom_commune = ""
    equipement_id = 0
    nb_equipement = 0
    code_activite = 0
    nom_activite = ""

    def __init__(self, code_postale, nom_commune, equipement_id, nb_equipement, code_activite, nom_activite):
        self.code_postale = code_postale
        self.nom_commune = nom_commune
        self.equipement_id = equipement_id
        self.nb_equipement = nb_equipement
        self.code_activite = code_activite
        self.nom_activite = nom_activite

activiteList = []

def readCSV():
    with open("../initial/activites.csv","r") as file:
        reader = csv.reader(file)
        for row in reader:
            activiteList.append(Activite(row[0],row[1],row[2],row[3],row[4],row[5]));
        for elt in activiteList:
            elt.toString();
