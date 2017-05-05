#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv
from Equipement import Equipement
from Installation import Installation
from Activity import Activity
from Activity_Equipement import Activity_Equipement

def readcsv_installation():
    installationList = []
    with open("../initial/installations.csv","r") as file:
        reader = csv.reader(file)
        for row in reader:
            installationList.append(Installation(row[0],row[1],row[2],row[4],row[5]+" "+row[6],row[9],row[10], row[12]))
    return installationList #Return the list of installation

def readcsv_activity():
    activityList = []
    with open("../initial/activites.csv","r") as file:
        reader = csv.reader(file)
        for row in reader:
            activityList.append(Activity(row[4],row[5]))
    return activityList #Return the list of activity

def readcsv_equipement():
    equipementList=[]
    with open("../initial/equipements.csv","r") as file:
        reader = csv.reader(file)
        for row in reader:
            equipementList.append(Equipement(row[2],row[4],row[5]))
    return equipementList #Return the list of equipement

def create_activity_equipement_list():
    activity_equipementList = []
    with open("../initial/activites.csv","r") as file:
        reader = csv.reader(file)
        for row in reader:
            activity_equipementList.append(Activity_Equipement(row[2],row[4]))
    return activity_equipementList #Return the list of activity
