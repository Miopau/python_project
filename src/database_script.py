#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Importation of library
import sqlite3, os

# current path file
dir_path = os.path.dirname(os.path.realpath(__file__))
list = []

"""
    function to get all activity from selected city or zip code
    :param var: city or zip code
    :return: list of activity
"""
def find_activity_from_city_zip_code(var):
    try:
        conn = sqlite3.connect('{}/../data/project_database.db'.format(dir_path))
        cursor = conn.cursor()

        if isinstance(var,int) :
            cursor.execute("""SELECT distinct name FROM activity where
                number in(SELECT activity_number from activity_equipement
                where equipement_number in(SELECT number from equipement
                where installation_number in (SELECT number from installation
                where zip_code=?)))""", (var,))
        else:
            cursor.execute("""SELECT distinct name FROM activity where
                number in(SELECT activity_number from activity_equipement
                where equipement_number in(SELECT number from equipement
                where installation_number in (SELECT number from installation
                where city LIKE ?)))""", (var,))

        for row in cursor:
            list.append(row[0])

    except Exception as e:
        print("ERREUR:")
        print (e)
        print ("\n")

    finally:
        conn.close()
        return list

"""
    function to get all activity
    :return: list of activity
"""
def list_activity():
    try:
        conn = sqlite3.connect('{}/../data/project_database.db'.format(dir_path))
        cursor = conn.cursor()

        cursor.execute("""SELECT distinct name FROM activity ORDER BY name""")

        for row in cursor:
            list.append(row[0])

    except Exception as e:
        print("ERREUR:")
        print (e)
        print ("\n")

    finally:
        conn.close()
        return list

"""
    function to get all city from activity
    :return: list of city
"""
def get_city(activity):
    try:
        conn = sqlite3.connect('{}/../data/project_database.db'.format(dir_path))
        cursor = conn.cursor()

        cursor.execute("""SELECT distinct name,city,adress,zip_code FROM installation where
        number in (SELECT installation_number from equipement where
        number in (SELECT equipement_number number from activity_equipement where
        activity_number in (SELECT number from activity where name LIKE ?)))""", (activity,))

        for row in cursor:
            l = []
            l.append(row[0])
            l.append(row[1])
            l.append(row[2])
            l.append(row[3])
            list.append(l)

    except Exception as e:
        print("ERREUR:")
        print (e)
        print ("\n")

    finally:
        conn.close()
        return list

"""
    function to get latitude and longitude for activity
    :return: list latitude and longitude
"""
def get_coord(city,adress,zipcode,name):
    try:
        conn = sqlite3.connect('{}/../data/project_database.db'.format(dir_path))
        cursor = conn.cursor()

        cursor.execute("""SELECT latitude, longitude FROM installation
        where city=? and adress=? and zipcode=? and name=?""", (city,adress,zipcode,name,))

        for row in cursor:
            list.append(row)

    except Exception as e:
        print("ERREUR:")
        print (e)
        print ("\n")

    finally:
        conn.close()
        return list

if __name__ == "__main__":
    for e in get_city("aviron"):
        print (e)
