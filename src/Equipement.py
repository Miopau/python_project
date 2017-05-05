#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv

class Equipement:
    """
    Variable and class declaration
    """
    installation_id = 0
    equipement_id = 0
    nom_equipement = ""


    def __init__(self, installation_id, equipement_id, nom_equipement):
        """
        Construct function of the class
        """
        self.installation_id = installation_id
        self.equipement_id = equipement_id
        self.nom_equipement = nom_equipement

# #Initialisation of the list
# equipementList = []
#
#
# def readCSV():
#     """
#     Function that read the csv and create Installation list
#     """
#     with open("../initial/equipements.csv","r") as file:
#         reader = csv.reader(file)
#         for row in reader:
#             equipment = Equipement(row[2],row[4],row[5])
#             equipementList.append(equipment);
#         return equipementList #Return the list of equipement
#
# ##      TEST
# for a in readCSV():
#     print (a.installation_id)
#     print (a.equipement_id)
#     print (a.nom_equipement)
#     print ( "\n\n\n")
