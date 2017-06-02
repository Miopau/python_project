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

        cursor.execute("""SELECT distinct name FROM activity""")

        for row in cursor:
            list.append(row[0])

    except Exception as e:
        print("ERREUR:")
        print (e)
        print ("\n")

    finally:
        conn.close()
        return list

if __name__ == "__main__":
    l= find_activity_from_city_zip_code("Nantes")
    for row in l:
        print(row)

    # ll= list_activity()
    # for row in ll:
    #     print(row)
