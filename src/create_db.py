#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('../data/project_database.db')

cursor = conn.cursor()

cursor.execute("""
DROP TABLE equipement_activites
""")

cursor.execute("""
DROP TABLE equipements
""")

cursor.execute("""
DROP TABLE installations
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS activites(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     age INTERGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS equipements(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     age INTERGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS installations(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     age INTERGER
)
""")

conn.commit()
conn.close()
