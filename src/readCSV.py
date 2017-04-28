#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv,Equipement,Installation,Activity

def readcsv(files,*args):
    equipementList = []
    with open(files,"r") as file:
        reader = csv.reader(file)
        for row in reader:
            equipment = Equipement(args)
            equipementList.append(equipment);
        return equipementList #Return the list of equipement
