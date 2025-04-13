# Utilise une image officielle Python comme base
FROM python:3.12-slim

# Définir le dossier de travail dans le conteneur
WORKDIR /app

# Copier les fichiers du projet dans le conteneur
COPY . .

# Installer les dépendances (si tu as un requirements.txt, sinon tu peux sauter cette ligne)
# RUN pip install -r requirements.txt

# Lancer les tests automatiquement à la construction (optionnel)
# RUN python -m unittest discover

# Commande par défaut (ici : lance les tests pour l’exemple)
CMD ["python", "-m", "unittest", "discover"]
