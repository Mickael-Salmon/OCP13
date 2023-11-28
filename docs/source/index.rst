.. OC Lettings Site documentation master file, created by
   sphinx-quickstart on Sun Nov 19 14:44:45 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to OC Lettings Site's documentation!
============================================
Le projet OCP13 est une application web Django conçue pour ...

Objectifs
==========

Objectif 1 - Améliorez l'architecture modulaire
-----------------------------------------------

**Penser à la réusabilité et la maintenance :**
Chaque application Django (oc\_letting\_site, profile, letting) devrait être conçue pour être aussi indépendante que possible.
Cela facilite la réutilisation dans d'autres projets et simplifie la maintenance.

**Tests Unitaires :**
S'assurer que chaque application a ses propres tests unitaires pour vérifier son bon fonctionnement de manière isolée.

Objectif 2 - Réduire la dette technique et les problèmes sur le projet
----------------------------------------------------------------------
**Utilisation de linters et formatters :**
Des outils comme Flake8, Black et isort peuvent grandement améliorer la qualité et la cohérence du code.

**Attention aux faux positifs en couverture de test :**
Parfois, avoir une couverture de test élevée ne signifie pas que tous les cas sont bien testés.
Nous visons donc une couverture significative qui teste réellement les fonctionnalités clés.


Objectif 3 - Surveiller l'application avec Sentry
--------------------------------------------------
**Environnements de staging et production :**
Sentry est bien configuré différemment pour les environnements de staging et de production pour éviter la confusion dans les rapports d'erreurs.
**Alertes Proactives :**
Configuration des alertes pour être informé en temps réel des problèmes critiques.

Objectif 4 - Mise en place le pipeline CI/CD et le déploiement
--------------------------------------------------------------
**Automatisation des tests :**
La CI exécute tous les tests automatiquement et fournit des retours clairs en cas d'échec.
**Gestion des secrets et variables d'environnement :**
Utilisation de Docker et Docker Compose pour gérer les secrets et les variables d'environnement.



Installation
============

Prérequis
---------

* Python 3.9.x
* Django 3.0.x
* Contenu de requirements.txt
*

Étapes d'Installation
---------------------

1. Fork et Cloner le dépôt :

**Fork du projet :**
Depuis GitHub, utilisation de la fonction "Fork" sur la page du projet.

**Clone du projet :**

   .. code-block:: bash

      git clone https://github.com/Mickael-Salmon/OCP13

1. Installer un environnement virtuel et les dépendances :

   .. code-block:: bash

      python -m venv .venv
      source .venv/bin/activate
      pip install -r requirements.txt

2. Lancer l'application pour déterminer le bon fonctionnement du Fork initial :

   .. code-block:: bash

      python manage.py runserver

3. Se connecter à l'application :

   .. code-block:: bash

      http://localhost:8000/

Création de 3 applications distinctes
-------------------------------------

Guide de Démarrage Rapide
=========================

Pour lancer l'application en mode développement :

.. code-block:: bash

   python manage.py runserver

Structure de l'Application
===========================

Applications Django
-------------------

* ``letting``

  * Description de ``letting``

* ``profiles``

  * Description de ``profiles``

* ``oc_letting_site``

  * Description de ``oc_letting_site``

Modèles de Données
------------------

Modèle ``Letting``
^^^^^^^^^^^^^^^^^^

* Champ 1
* Champ 2

Modèle ``Profile``
^^^^^^^^^^^^^^^^^^

* Champ A
* Champ B

Guide d'Utilisation
===================

Fonctionnalités Principales
---------------------------

* Fonctionnalité 1
* Fonctionnalité 2

Exemples d'Utilisation
----------------------

1. Exemple 1
2. Exemple 2

Déploiement
===========

Environnement de Production
---------------------------

* Serveur Web
* Base de données

Étapes de Déploiement
---------------------

1. Étape 1
2. Étape 2
