#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3, os

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    try:
        conn = sqlite3.connect('{}/../data/project_database.db'.format(dir_path))
        cursor = conn.cursor()

        #cleaning database
        clean(cursor)

        #create TABLE
        create(cursor)

        conn.commit()
    except Exception as e:
        print("ERREUR:")
        print (e)
        print ("\n")

    finally:
        conn.close()


def clean(cursor):
    cursor.execute("""DROP TABLE IF EXISTS activity_equipement""")
    cursor.execute("""DROP TABLE IF EXISTS installation""")
    cursor.execute("""DROP TABLE IF EXISTS equipement""")
    cursor.execute("""DROP TABLE IF EXISTS activity""")

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
