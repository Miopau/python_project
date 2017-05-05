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
