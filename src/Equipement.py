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
