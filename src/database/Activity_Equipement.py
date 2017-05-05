#!/usr/bin/env python3pass
# -*- coding: utf-8 -*-

class Activity_Equipement:
    """
    Variable and class declaration
    """
    equipementID=0;
    activityID=0;

    def __init__(self, equipementID, activityID):
        """
        Construct function of the class
        """
        self.equipementID=equipementID
        self.activityID=activityID
