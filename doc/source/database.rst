Base de donnée
==============

.. contents::
   :depth: 4
   :local:

.. image:: https://upload.wikimedia.org/wikipedia/commons/3/38/SQLite370.svg
      :height: 495
      :width: 934
      :alt: SQLite3 logo

.. role:: raw-html(raw)
    :format: html

:raw-html:`<br />`

*SQLite3*
---------

SQLite3 est une bibliothèque écrite en langage C qui propose un moteur de base de données relationnelle accessible par le langage SQL.

Il s'agit d'une base de données légère stockée sur disque, ne nécessitant pas de processus serveur distinct, et permettant d'accéder à la base de données à l'aide d'une variante non standard du langage de requête SQL.

SQLite est largement utilisé dans de nombreux logiciels grand public, ainsi que dans certains produits d'Apple, d'Adobe et de McAfee.
Il est également intégré dans les bibliothèques standards de nombreux langages comme PHP ou Python.

SQLite3 prend en charge des fonctionnalités avancées telles que la gestion des clés étrangères, les contraintes CHECK, les normes UTF-8 et UTF-16, et encode les identifiants de lignes sur 64 bits.

*Pourquoi utiliser SQLite3 ?*
-----------------------------

SQLite3 présente plusieurs avantages par rapport à d'autres systèmes de gestion de base de données relationnelles (SGBDR) tels que PostgreSQL et MySQL.

Voici quelques-uns de ces avantages :
Embarqué et sans serveur : Contrairement à PostgreSQL et MySQL, SQLite3 est un SGBDR embarqué et sans serveur, ce qui signifie qu'il ne nécessite aucune installation ou configuration de serveur distincte.
Il peut être intégré directement dans l'application elle-même.

**Légèreté** : SQLite3 est très léger en termes de taille et de ressources requises, ce qui le rend idéal pour les applications avec des besoins de stockage de données plus modestes.

**Facilité d'utilisation** : SQLite3 est convivial et facile à utiliser, ce qui en fait un bon choix pour les applications qui nécessitent une mise en œuvre rapide et simple de la gestion des données.

**Performances dans des environnements à faible mémoire** : SQLite3 offre de bonnes performances même dans des environnements à faible mémoire, ce qui le rend adapté à des applications avec des contraintes de ressources

Présentation des objets et de l'ERD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Entité
     - Champs
     - Description
     - Relations
   * - Profile
     - id, email, name
     - Représente un client.
     - Lié à 'User'
   * - Letting
     - id, title, description
     - Représente une annonce de location.
     - Lié à 'Address'
   * - Address
     - id, street, city, zip_code, country
     - Représente une propriété à louer.
     -


Présentation des modèles
------------------------

**Profile : Représentant un client.**
-------------------------------------

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Classe
     - Description
   * - Profile
     - .. autoclass:: profiles.models.Profile
          :members:
          :no-index:

**Letting : Représentant une location.**
----------------------------------------
.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Classe
     - Description
   * - Letting
     - .. autoclass:: letting.models.Letting
          :members:
          :no-index:

**Address : Représentant une propriété à louer.**
-------------------------------------------------

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Classe
     - Description
   * - Address
     - .. autoclass:: letting.models.Address
          :members:
          :no-index:

