# Google Workspace User List Script

This Python script retrieves and displays a list of users from a Google Workspace domain using the Google Admin SDK. It utilizes a service account to authenticate and access the directory information in read-only mode.

## Prerequisites

Before you can run this script, ensure you have the following set up:

1. **Google Cloud Project**:
   - Create a project in the [Google Cloud Console](https://console.cloud.google.com/).
   - Enable the Admin SDK API for the project.

2. **Service Account**:
   - Create a service account in the Google Cloud Console.
   - Download the JSON key file for the service account.

3. **Domain-Wide Delegation**:
   - In the Google Workspace Admin Console, enable domain-wide delegation for the service account.
   - Add the service account's Client ID and grant it the necessary OAuth scopes:
     - `https://www.googleapis.com/auth/admin.directory.user.readonly`

4. **Python**:
   - Ensure Python is installed on your system.
   - Install the required Python packages:
     ```bash
     pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
     ```

## Setup

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/google-workspace-user-list.git
    cd google-workspace-user-list
    ```

2. Place your service account JSON key file in the project directory.

3. Update the script (`list_users.py`) with the path to your service account file and your Google Workspace admin email:

    ```python
    SERVICE_ACCOUNT_FILE = 'path/to/your-service-account-file.json'
    ADMIN_EMAIL = 'admin@yourdomain.com'
    ```

## Running the Script

To run the script, use the following command:

```bash
python main.py
