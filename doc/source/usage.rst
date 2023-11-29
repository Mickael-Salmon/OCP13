Usage
=====

.. contents::
   :depth: 4
   :local:


*Chemins URL d'accès du site*
-----------------------------

- **Adresse du site Django admin :**

Pour accéder au site admin utiliser l'adresse *'/admin/'*



`Lien vers le site admin <https://oc-letting-site.onrender.com/admin/>`_

- **Adresse test sentry :**

Afin de tester grace à une erreur de division par zero, que la liaison avec Sentry est bien effective, il suffit d'aller à l'adresse suivante du site :
*'/sentry-debug/'*.

`Lien vers le site <https://oc-letting-site.onrender.com/sentry-debug/>`_


*Workflow de développement - déclencheur*
-----------------------------------------

.. _workflow-description:

Description du Workflow
=======================

Ce document décrit le workflow complet depuis le développement local jusqu'au déploiement sur RENDER, en utilisant GitHub, CircleCI et DockerHub.

Développement local
-------------------

1. **Développement et tests** :
   Le développement se fait localement. Après avoir écrit et testé le code, effectuer les tests unitaires et d'intégration pour s'assurer de la qualité du code.

2. **Commit et Push sur GitHub** :
   Une fois le développement et les tests terminés, les modifications sont enregistrées (commit) et poussées (push) sur le dépôt GitHub.

GitHub
------

- **Dépôt de code source** :
  GitHub sert de dépôt central pour le code source. Chaque push déclenche des actions définies dans le pipeline de CI/CD.

CircleCI
--------

1. **Intégration et déploiement continu** :
   CircleCI est configuré pour détecter chaque push sur le dépôt GitHub. Il démarre alors les processus d'intégration et de déploiement continu.

2. **Construction du Docker** :
   CircleCI construit une image Docker basée sur le code source actuel. Cette image est ensuite testée pour s'assurer qu'elle fonctionne comme prévu.

DockerHub
---------

- **Stockage d'images Docker** :
  Une fois que CircleCI a construit et testé l'image Docker avec succès, cette image est poussée et stockée sur DockerHub.

RENDER
------

1. **Déploiement** :
   RENDER est utilisé pour le déploiement final. Les nouvelles images Docker disponibles sur DockerHub peuvent être déployées manuellement ou automatiquement sur RENDER.

2. **Mise en production** :
   Une fois l'image déployée sur RENDER, l'application est maintenant en production et accessible aux utilisateurs finaux.

Ce workflow assure un processus de développement, de test, d'intégration et de déploiement efficace et automatisé, garantissant ainsi une qualité et une fiabilité élevées de l'application déployée.







