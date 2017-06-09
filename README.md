# Installations Sportives des Pays de la Loire

Le langage de programmation utilisé pour le projet est [Python](https://www.python.org), en version 3.
Ce Projet à été réalisé dans le cadre d'une formation de DUT informatique à l'IUT de Nantes.

## Le projet

L'objectif est de développer une application manipulant des données relatives aux installations sportives de la région Pays de la Loire.


## Faire fonctionner le projet
Afin de démarrer notre interface il faut tout d'abord clonner ce projet.
```
        git clone https://github.com/Miopau/python_project.git
```

Ensuite afin creer la base de données et de la replir il faut se placer dans le dossier src/database/ puis executer le script create_db.py. La base de donnée SQLite se trouvera une fois créée dans data/

```
        python3 create_db.py
```
Si vous voulez mettre à jour les données il suffit de remplacer les 3 fichier CSV placé dans initial/ <br/>

Maintenant il faut lancer le serveur. Se placer dans src/ et lancer le script serv.py
```
        python3 serv.py
```

Vous pouvez maintenant vous connecter à l'adresse suivante http://localhost:8085/index et naviguer sur le site.

## Documentation utilisé nécessaire à la réalisation du projet

### Documentation du projet:
Cours: <br/> http://nsal.im/iut/techno/#/ <br/>
Doc: <br/> https://github.com/sebprunier/installations-sportives-pdl<br/>
SQLLite Doc: <br/>
http://apprendre-python.com/page-database-data-base-donnees-query-sql-mysql-postgre-sqlite


### Objectifs :

#### Partie 1 :

Module 1 (import des données) :
        * définit quelques classes simples (une pour Installation, Equipement,Activité)
        * lit les fichiers CSV / JSON
        * créé un objet pour chaque élément du fichier

#### Partie 2 :

Module 1 (administration de la base) :
        * supprime si existe puis créé une base de données SQLite

Module 2 (import des données) :
        * les objets sont insérés en base

Module 3 (test de la base) :
        * lit les objets en base et affiche leur contenu
