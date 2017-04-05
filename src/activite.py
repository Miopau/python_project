#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

class Activity:
    activityID = 0
    activityName = ""

    def __init__(self, activityID, activityName):
        self.activityID = activityID
        self.activityName = activityName

activiteList = []

def readCSV():
    with open("../initial/activites.csv","r") as file:
        reader = csv.reader(file)
        for row in reader:
            activiteList.append(Activite(row[4],row[5]));
