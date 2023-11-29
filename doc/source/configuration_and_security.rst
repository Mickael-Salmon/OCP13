Configuration et sécurité
=========================

.. contents::
   :depth: 4
   :local:

.. _Django:

*Django*
--------


Django settings:
^^^^^^^^^^^^^^^^

`Documentation Django <https://docs.djangoproject.com/fr/4.2/ref/settings/>`_


**IMPORTANT**
--------------

. Création et Configuration du Fichier .env
Crée un fichier .env à la racine de ton projet Django. Ce fichier contiendra tes variables d'environnement.
Dans ton fichier .env, ajoute tes clés secrètes :

.. code-block:: shell

    SECRET_KEY=ta_super_clé_secrète_django
    SENTRY_DSN=ton_url_dsn_sentry

Ajoute .env à ton .gitignore pour éviter de le pousser sur GitHub :


1. Modification du settings.py de Django
Tu dois ensuite modifier ton fichier settings.py pour utiliser ces variables d'environnement.

Installe python-decouple pour gérer les variables d'environnement :
.. code-block:: shell

   pip install python-decouple


Ensuite, modifie ton settings.py pour utiliser python-decouple :
python

.. code-block:: python

    from decouple import config
    from decouple import AutoConfig

    config = AutoConfig(search_path=None)  # Charger automatiquement le fichier .env


# Plus bas dans ton fichier settings.py

.. code-block:: python

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = config('SECRET_KEY')

    # Sentry configuration
    sentry_sdk.init(
    dsn=config('SENTRY_DSN', default=""),
    # Tes autres configurations...
    )

3. Utilisation des Variables d'Environnement dans CircleCI
Pour que CircleCI utilise ces variables, ajoute-les dans les paramètres de ton projet sur CircleCI.
Il va les récupérer lors de la construction et du déploiement.

4. Exemple de Fichier .env

Ton fichier .env ressemblera à ceci :

.. code-block:: shell

    dotenv
    SECRET_KEY=ta_super_clé_secrète_django
    SENTRY_DSN=ton_url_dsn_sentry

`Secret Key documentation <https://docs.djangoproject.com/fr/4.2/ref/settings/#std-setting-SECRET_KEY>`_


**DEBUG**
---------

.. code-block:: python

                    # SECURITY WARNING: don't run with debug turned on in production!

                    DEBUG = bool(os.environ.get('DEBUG', default=False))
                    ALLOWED_HOSTS = ['oc-letting-site.onrender.com',
                                     '127.0.0.1',
                                     'localhost',
                                    ]


* Il est recommandé de passer DEBUG à FALSE en production. En effet, si DEBUG est à TRUE, Django affiche les erreurs
  de l'application, ce qui peut être utile en développement mais pas en production.
* Il est recommandé de passer ALLOWED_HOSTS à une liste d'adresses autorisées en production. En effet, si ALLOWED_HOSTS est
  vide, Django autorise toutes les adresses, ce qui peut être utile en développement mais pas en production. Ici on a ajouté RENDER en plus des adresses locales.


**WhiteNoise**:
----------------

`WhiteNoise <https://whitenoise.readthedocs.io/en/latest/django.html>`_

WhiteNoise est un outil qui permet de servir les fichiers statiques d'une application web Python, en particulier avec Django.
Il simplifie le processus de gestion des fichiers statiques en les servant directement à partir de l'application web, sans avoir besoin de recourir à des services externes tels que Nginx ou Amazon S3.

WhiteNoise s'intègre bien avec un CDN pour les sites à fort trafic, et prend en charge la compression des fichiers et la mise en cache avec des en-têtes de cache à long terme pour les contenus statiques qui ne changent pas.

Pour l'utiliser avec Django, il suffit d'ajouter WhiteNoise au paramètre MIDDLEWARE dans le fichier settings.py, juste au-dessus de tous les autres middlewares, à l'exception de ceux de Django.
Ensuite, il faut spécifier le répertoire racine des fichiers statiques en utilisant la variable STATIC_ROOT dans le fichier settings.py.

Enfin, il est recommandé d'utiliser WhiteNoise également en environnement de développement pour éviter les différences de comportement entre les environnements de développement et de production.


Afin d'utiliser whitenoise : (à insérer dans settings.py)

.. code-block:: python

                    MIDDLEWARE = [
                        'django.middleware.security.SecurityMiddleware',
                        'whitenoise.middleware.WhiteNoiseMiddleware',
                        ...
                    ]

.. code-block:: python

                    # Static files (CSS, JavaScript, Images)
                    # https://docs.djangoproject.com/en/3.0/howto/static-files/

                    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

                    STATIC_URL = 'staticfiles/'
                    STATICFILES_DIRS = [BASE_DIR / "static", ]

                    STORAGES = {
                        "default": {
                            "BACKEND": "django.core.files.storage.FileSystemStorage",
                        },
                        "staticfiles": {
                            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
                        },
                    }




**Sentry**:
------------

Sentry est un outil de gestion des erreurs qui se concentre principalement sur la capture des exceptions d'application, telles que les plantages d'application, et non sur la journalisation générale.

Contrairement à la journalisation traditionnelle, qui fournit une trace des événements, y compris les erreurs et les informations, Sentry se concentre sur la capture des erreurs d'application et ne remplace pas la nécessité de la journalisation.

Il complète souvent l'infrastructure de journalisation existante en capturant des problèmes spécifiques du code.
De plus, Sentry stocke moins de détails sur chaque erreur pour économiser de l'espace, ce qui signifie qu'il ne garantit pas la possibilité de retrouver exactement une erreur historique.

En résumé, Sentry fonctionne avec l'infrastructure de journalisation de l'application, souvent en s'intégrant directement, mais ne remplace pas la journalisation générale.

En Python, Sentry propose une intégration de journalisation qui permet de capturer les messages de journalisation et de les envoyer à Sentry en tant qu'événements.
Cette intégration peut être configurée pour enregistrer les messages de journalisation avec un niveau supérieur à un certain seuil en tant que miettes de pain, et pour envoyer les erreurs en tant qu'événements à Sentry.

(à insérer dans settings.py)

.. code-block:: python


                    def profiles_sampler(sampling_context):
                        # ...
                        # return a number between 0 and 1 or a boolean
                        return True

                    sentry_sdk.init(
                        dsn=os.environ.get('DSN'),
                        # Set traces_sample_rate to 1.0 to capture 100%
                        # of transactions for performance monitoring.
                        # We recommend adjusting this value in production.
                        traces_sample_rate=1.0,
                        # Set profiles_sample_rate to 1.0 to profile 100%
                        # of sampled transactions.
                        # We recommend adjusting this value in production.
                        profiles_sample_rate=1.0,

                        # Alternatively, to control sampling dynamically
                        profiles_sampler=profiles_sampler,
                        integrations=[
                            DjangoIntegration(
                                transaction_style='url',
                                middleware_spans=True,
                                signals_spans=True,
                                cache_spans=True,
                            ),
                        ],
                        send_default_pii=True
                    )

Actuellement 100% des erreurs sont capturées dans Sentry.

Variable d'environnement stockée dans .env :
.. envvar:: SENTRY_DSN



`Documentation officielle Sentry Platform Django <https://docs.sentry.io/platforms/python/guides/django>`_

**Gunicorn**:
--------------

Déploiement de Django avec Gunicorn :

`Gunicorn <https://gunicorn.org/>`_ (« Green Unicorn ») Gunicorn est un serveur web HTTP pour UNIX, utilisé principalement pour servir des applications Python via l'interface WSGI (Web Server Gateway Interface). Il s'agit d'un serveur pré-fork, ce qui signifie qu'il crée un ensemble de processus de travail au démarrage pour gérer les requêtes. Gunicorn est compatible avec divers frameworks web, léger en termes de ressources serveur et assez rapide.
Il est souvent utilisé en combinaison avec des serveurs proxy HTTP tels que Nginx pour améliorer les performances.

La configuration se trouve dans le fichier *dockerfile*, situé à la racine du projet, comme ceci :

.. warning::

          Gunicorn s'exécute seulement sous un system UNIX.

.. code-block:: python

                    CMD gunicorn --bind=0.0.0.0:8080 --timeout 200 oc_lettings_site.wsgi






**Hébergement en CLOUD - Solution retenue RENDER**
---------------------------------------------------


`Documentation officielle Render <https://render.com/docs>`_


Render est une solution d'hébergement infonuagique unifiée qui permet de construire et d'exécuter toutes vos applications et sites web avec des certificats TLS gratuits, un CDN mondial, des réseaux privés et des déploiements automatiques à partir de Git.
Il offre une grande facilité d'utilisation combinée à une immense puissance et évolutivité pour tout, des simples pages HTML aux applications complexes avec des centaines de microservices.
Render héberge des sites statiques, des API back-end, des bases de données, des tâches cron et toutes vos autres applications au même endroit.
Les sites statiques sont entièrement gratuits sur Render et incluent des constructions et déploiements automatiques continus à partir de GitHub et GitLab, des certificats SSL automatiques via Let's Encrypt, une invalidation instantanée du cache avec un CDN mondial ultra-rapide, et bien plus encore...

