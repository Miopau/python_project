#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3, os, Activity, Equipement,Installation
from readCSV import readcsv_installation,readcsv_equipement,readcsv_activity

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
        # l_installation = readcsv_installation()

        #create objetc list of equipement
        l_equipement =[]
        # l_equipement= readcsv_equipement()

        #create objetc list of installation
        l_activity =[]
        # l_activity= readcsv_activity()


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
         longitude DECIMAL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS equipement(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
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

if __name__ == "__main__":
    main()
