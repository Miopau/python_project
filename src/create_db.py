#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3, os

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    conn = sqlite3.connect('{}/../data/project_database.db'.format(dir_path))
    cursor = conn.cursor()

    #cleaning database
    clean(cursor)

    #create TABLE
    create(cursor)

    conn.commit()
    conn.close()

def clean(cursor):
    cursor.execute("""DROP TABLE IF EXISTS equipement_activite""")
    cursor.execute("""DROP TABLE IF EXISTS installations""")
    cursor.execute("""DROP TABLE IF EXISTS equipement""")
    cursor.execute("""DROP TABLE IF EXISTS activite""")

def create(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS activite(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         name TEXT,
         age INTERGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS equipement(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         name TEXT,
         age INTERGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS installation(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         name TEXT,
         age INTERGER
    )
    """)

if __name__ == "__main__":
    main()
