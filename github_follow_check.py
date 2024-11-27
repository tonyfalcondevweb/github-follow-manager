from dotenv import load_dotenv
import os
import requests

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer les identifiants depuis les variables d'environnement
USERNAME = os.getenv("GITHUB_USERNAME")
TOKEN = os.getenv("GITHUB_TOKEN")

# Vérifier que les variables sont correctement chargées
if not USERNAME or not TOKEN:
    raise Exception("Les variables GITHUB_USERNAME ou GITHUB_TOKEN ne sont pas définies dans le fichier .env.")

# Fonction pour obtenir la liste des followers
def get_followers():
    url = f"https://api.github.com/users/{USERNAME}/followers"
    response = requests.get(url, auth=(USERNAME, TOKEN))
    response.raise_for_status()  # Vérifie si la requête a réussi
    return [user['login'] for user in response.json()]

# Fonction pour obtenir la liste des following
def get_following():
    url = f"https://api.github.com/users/{USERNAME}/following"
    response = requests.get(url, auth=(USERNAME, TOKEN))
    response.raise_for_status()
    return [user['login'] for user in response.json()]

# Comparaison des followers et following
followers = get_followers()
following = get_following()
non_followers = [user for user in following if user not in followers]

print("Users you follow but who don't follow you back:", non_followers)
