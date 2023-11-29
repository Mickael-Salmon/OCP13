Déploiement et tests
====================

.. contents::
   :depth: 4
   :local:

Le processus workflow pipeline CircleCI consiste à reconstruire une image Docker, effectuer des tests depuis un commit sur GitHub, pousser cette image vers Docker Hub, puis la récupérer sur Render.
Pour ce faire, on peut utiliser la configuration YAML de CircleCI pour définir les étapes du pipeline, telles que la construction de l'image Docker, l'exécution des tests, et le déploiement vers Docker Hub.

La configuration YAML de CircleCI permet d'automatiser le processus de test et de déploiement.
Par exemple, pour exécuter des tests dans un pipeline, on peut ajouter des clés de configuration dans le fichier .circleci/config.yml.

Ces clés définissent les étapes à exécuter dans un travail, telles que la construction de l'image Docker, l'exécution des tests, et le déploiement vers Docker Hub.
En utilisant la configuration YAML de CircleCI, on peut également intégrer des outils de test populaires tels que Jest, Mocha, pytest, JUnit, Selenium, XCTest, etc.

Ces outils permettent d'exécuter des tests automatiquement dans le pipeline, ce qui permet d'obtenir des retours plus rapides pour corriger les problèmes et les tests échoués plus rapidement.

*Workflow*
----------
.. _workflow-description:

Description du Workflow
=======================

Voici une description complète du workflow depuis le développement local jusqu'au déploiement sur RENDER, en utilisant GitHub, CircleCI et DockerHub.

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



*Tests*
-------


Linting
^^^^^^^

Flake8 est utilisé comme linter, qui respecte la PEP8.
La configuration est comme ceci :

voir `documentation officiel Flake8 <https://flake8.pycqa.org/en/latest/user/options.html#cmdoption-flake8-count>`_

setup.cfg

.. code-block:: python

                    [flake8]
                    max-line-length = 99
                    exclude =
                     ... fichiers/repertoires exclus du linting
                    tee = True
                    output-file=reports/flake8/flake8stats.txt
                    format= html
                    statistics = True
                    htmldir = reports/flake8/
                    show_source = True



Tests unitaires
^^^^^^^^^^^^^^^

Les tests unitaires sont configuré avec pytest.

`Documentation officiel de pytest <https://docs.pytest.org/en/stable/contents.html>`_

setup.cfg

.. code-block:: python

                    [tool:pytest]
                    DJANGO_SETTINGS_MODULE = oc_lettings_site.settings
                    python_files = tests.py
                    addopts = -v --no-migrations


--no migration : `pytest-django <https://pytest-django.readthedocs.io/en/latest/database.html>`_


Couverture
^^^^^^^^^^

La couverture des tests unitaires couvre 80% du code et est déclenchée à chaque docker build pour garantir le bon fonctionnement du code avant de pousser en production sur RENDER.




