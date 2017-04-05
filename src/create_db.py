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
    cursor.execute("""DROP TABLE IF EXISTS equipement_activite""")
    cursor.execute("""DROP TABLE IF EXISTS installation""")
    cursor.execute("""DROP TABLE IF EXISTS equipement""")
    cursor.execute("""DROP TABLE IF EXISTS activite""")

def create(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS equipement_activite(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         numero_equipement INTEGER,
         numero_activite INTERGER,
         FOREIGN KEY(numero_equipement) REFERENCES equipement(numero),
         FOREIGN KEY(numero_activite) REFERENCES activite(numero)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS installation(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         numero INTEGER,
         nom TEXT,
         adresse TEXT,
         code_postal TEXT,
         ville TEXT,
         latitude DECIMAL,
         longitude DECIMAL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS equipement(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         nom TEXT,
         numero_installation INTERGER,
         FOREIGN KEY(numero_installation) REFERENCES installation(numero)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS activite(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         numero INTEGER,
         nom TEXT
    )
    """)

if __name__ == "__main__":
    main()
