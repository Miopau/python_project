#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Importation of library
import sqlite3, os, Activity, Equipement,Installation
from readCSV import readcsv_installation,readcsv_equipement,readcsv_activity,create_activity_equipement_list

"""
    Main function who:
        - create database
        - drop all TABLES
        - create new TABLES
        - fill TABLES whith clean data
"""
def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    try:
        conn = sqlite3.connect('{}/../data/project_database.db'.format(dir_path))
        cursor = conn.cursor()

        #cleaning database
        clean(cursor)

        #create TABLE
        create(cursor)

        #create objetc list of installation
        l_installation =[]
        l_installation = readcsv_installation()

        #create objetc list of equipement
        l_equipement =[]
        l_equipement= readcsv_equipement()

        #create objetc list of installation
        l_activity =[]
        l_activity= readcsv_activity()

        l_activity_equipement = []
        l_activity_equipement = create_activity_equipement_list()

        insert(cursor,l_activity,l_equipement,l_installation,l_activity_equipement)

        conn.commit()
    except Exception as e:
        print("ERREUR:")
        print (e)
        print ("\n")

    finally:
        conn.close()

"""
    function to clean all tables in database
    :param cursor: cursor of the database
"""
def clean(cursor):
    cursor.execute("""DROP TABLE IF EXISTS activity_equipement""")
    cursor.execute("""DROP TABLE IF EXISTS installation""")
    cursor.execute("""DROP TABLE IF EXISTS equipement""")
    cursor.execute("""DROP TABLE IF EXISTS activity""")

"""
    function to create all tables in database
    :param cursor: cursor of the database
"""
def create(cursor):
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

"""
    function to insert all data in table
    :param cursor: cursor of the database
    :param list_activity: list of activity object to parse
    :param list_equipment: list of equipment object to parse
    :param list_installation: list of installation object to parse
"""
def insert(cursor,list_activity,list_equipment,list_installation,list_activity_equipement):

    #INSERT INTO users(name, age) VALUES(?, ?)""", ("olivier", 30)

    #data = {"name" : "olivier", "age" : 30}
    #cursor.execute("""
    #INSERT INTO users(name, age) VALUES(:name, :age)""", data)

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
