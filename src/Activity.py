#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv

class Activity:
    """
    Variable and class declaration
    """
    activityID = 0
    activityName = ""

    def __init__(self, activityID, activityName):
        """
        Construct function of the class
        """
        self.activityID = activityID
        self.activityName = activityName

#     #Initialisation of the list
#     activityList = []
#
# def readCSV(l):
#     """
#     Function that read the csv and create Activity list
#     """
#     with open("../initial/activites.csv","r") as file:
#         reader = csv.reader(file)
#         for row in reader:
#             cols = []
#             for i in l:
#                 cols.append(row[i])
#             tuple(cols)
#             activiteList.append(Activite(cols.unpack()));
#         return activityList #Return the list of activity
