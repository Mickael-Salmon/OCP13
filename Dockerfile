# Utilisation de l'image officielle Python 3.9
FROM python:3.9

# Définition de l'environnement pour empêcher Python de générer des fichiers .pyc dans le conteneur
ENV PYTHONUNBUFFERED 1

# Création du répertoire de travail dans le conteneur
RUN mkdir /code

# Définition du répertoire de travail
WORKDIR /code

# Copie du fichier requirements.txt dans le conteneur
COPY requirements.txt /code/

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copie du reste des fichiers du projet dans le conteneur
COPY . /code/

# Commande pour exécuter l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
