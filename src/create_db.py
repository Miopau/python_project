#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('../data/project_database.db')

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS equipement_activites(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     age INTERGER
)
CREATE TABLE IF NOT EXISTS equipements(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     age INTERGER
)
CREATE TABLE IF NOT EXISTS installations(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     age INTERGER
)
""")

conn.commit()
db.close()
