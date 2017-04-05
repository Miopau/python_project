#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv

class Activity:
    activityID = 0
    activityName = ""

    def __init__(self, activityID, activityName):
        self.code_postale = code_postale
        self.nom_commune = nom_commune
        self.equipement_id = equipement_id
        self.nb_equipement = nb_equipement
        self.activityID = activityID
        self.activityName = activityName

activiteList = []

def readCSV():
    with open("../initial/activites.csv","r") as file:
        reader = csv.reader(file)
        for row in reader:
            activiteList.append(Activite(row[0],row[1],row[2],row[3],row[4],row[5]));
