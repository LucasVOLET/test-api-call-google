from google.oauth2 import service_account
from googleapiclient.discovery import build

# Chemin vers le fichier JSON du compte de service
SERVICE_ACCOUNT_FILE = 'credentials.json'

# Les portées nécessaires pour lire les utilisateurs
SCOPES = ['https://www.googleapis.com/auth/admin.directory.user.readonly']

# L'adresse email de l'administrateur pour lequel les permissions ont été déléguées
ADMIN_EMAIL = 'lucas.volet@oremis.fr'

# Charger les informations d'identification du compte de service
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Déléguer les autorisations au compte administrateur
delegated_credentials = credentials.with_subject(ADMIN_EMAIL)

# Construire le service Admin SDK
service = build('admin', 'directory_v1', credentials=delegated_credentials)

# Appel à l'API pour obtenir la liste des utilisateurs
results = service.users().list(customer='my_customer', maxResults=100, orderBy='email').execute()
users = results.get('users', [])

# Afficher la liste des utilisateurs
if not users:
    print('No users found.')
else:
    print('Users:')
    for user in users:
        print(f"User: {user['primaryEmail']}, Name: {user['name']['fullName']}")
