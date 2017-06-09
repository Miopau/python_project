#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Importation of library
import sqlite3, os, Activity, Equipement,Installation
from readCSV import readcsv_installation,readcsv_equipement,readcsv_activity,create_activity_equipement_list

def main():
    """
    Main function who:
    - create database
    - drop all TABLES
    - create new TABLES
    - fill TABLES whith clean data
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))
    try:
        conn = sqlite3.connect('{}/../../data/project_database.db'.format(dir_path))
        cursor = conn.cursor()

        #cleaning database
        clean(cursor)

        #create TABLE
        create(cursor)

        #create object list of installation
        l_installation =[]
        l_installation = readcsv_installation()

        #create object list of equipement
        l_equipement =[]
        l_equipement= readcsv_equipement()

        #create object list of installation
        l_activity =[]
        l_activity= readcsv_activity()

        #create object list of activity_equipement
        l_activity_equipement = []
        l_activity_equipement = create_activity_equipement_list()

        # Insert all data in database
        insert(cursor,l_activity,l_equipement,l_installation,l_activity_equipement)

        conn.commit()
    except Exception as e:
        print("ERROR:")
        print (e)
        print ("\n")

    finally:
        conn.close()

def clean(cursor):
    """
    function to clean all tables in database
    :param cursor: cursor of the database
    """
    cursor.execute("""DROP TABLE IF EXISTS activity_equipement""")
    cursor.execute("""DROP TABLE IF EXISTS installation""")
    cursor.execute("""DROP TABLE IF EXISTS equipement""")
    cursor.execute("""DROP TABLE IF EXISTS activity""")

def create(cursor):
    """
    function to create all tables in database
    :param cursor: cursor of the database
    """
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS activity_equipement(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         equipement_number INTEGER,
         activity_number INTERGER,
         FOREIGN KEY(equipement_number) REFERENCES equipement(number),
         FOREIGN KEY(activity_number) REFERENCES activity(number)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS installation(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         number INTEGER,
         name TEXT,
         adress TEXT,
         zip_code TEXT,
         city TEXT,
         latitude DECIMAL,
         longitude DECIMAL,
         disabledAdapted TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS equipement(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         number INTERGER,
         name TEXT,
         installation_number INTERGER,
         FOREIGN KEY(installation_number) REFERENCES installation(number)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS activity(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         number INTEGER,
         name TEXT
    )
    """)

def insert(cursor,list_activity,list_equipment,list_installation,list_activity_equipement):
    """
    function to insert all data in table
    :param cursor: cursor of the database
    :param list_activity: list of activity object to parse
    :param list_equipment: list of equipment object to parse
    :param list_installation: list of installation object to parse
    """

    for obj in list_installation:
        #insert to installation
        cursor.execute("""
        INSERT INTO installation(number,name,adress,zip_code,city,latitude,longitude,disabledAdapted) VALUES(?,?,?,?,?,?,?,?)
        """, (
        obj.installation_id,
        obj.installationName,
        obj.installationAdress,
        obj.zipCode,
        obj.cityName,
        obj.latitude,
        obj.longitude,
        obj.disabledAdapted)
        )

    for obj in list_equipment:
        # insert to equipement
        cursor.execute("""
        INSERT INTO equipement(number,name,installation_number) VALUES(?,?,?)
        """, (
        obj.equipement_id,
        obj.nom_equipement,
        obj.installation_id)
        )

    for obj in list_activity:
        # insert to activity
        cursor.execute("""
        INSERT INTO activity(number,name) VALUES(?,?)
        """, (
        obj.activityID,
        obj.activityName)
        )

    for obj in list_activity_equipement:
        # insert to activity_equipement
        cursor.execute("""
        INSERT INTO activity_equipement(equipement_number,activity_number) VALUES(?,?)
        """,(
        obj.equipementID,
        obj.activityID)
        )

if __name__ == "__main__":
    main()
