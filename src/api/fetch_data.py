import requests
import json
from datetime import datetime, timedelta
import os

def fetch_tsm_data():
    api_key = os.environ['API_KEY']
    auth_url = 'https://auth.tradeskillmaster.com/oauth2/token'
    alli_pricing_url = 'https://pricing-api.tradeskillmaster.com/ah/513'
    horde_pricing_url = 'https://pricing-api.tradeskillmaster.com/ah/514'

    payload = {
        "client_id": "c260f00d-1071-409a-992f-dda2e5498536",
        "grant_type": "api_token",
        "scope": "app:realm-api app:pricing-api",
        "token": api_key
    }

    # Authenticate
    response = requests.post(auth_url, json=payload)
    if response.status_code != 201:
        raise Exception(f"Authentication failed: {response.status_code}")

    auth_data = response.json()
    access_token = auth_data.get('access_token')
    headers = {'Authorization': f'Bearer {access_token}'}

    # Fetch pricing data
    alli_data = requests.get(alli_pricing_url, headers=headers).json()
    horde_data = requests.get(horde_pricing_url, headers=headers).json()

    # Structure data
    timestamp = datetime.utcnow().isoformat()
    data_entry = {
        'timestamp': timestamp,
        'alliance': alli_data,
        'horde': horde_data
    }

    # Load existing data
    data_file = 'data/pricing_data.json'
    if os.path.exists(data_file):
        with open(data_file, 'r') as f:
            existing_data = json.load(f)
    else:
        existing_data = []

    # Append new data
    existing_data.append(data_entry)

    # Keep only last 24 hours of data
    cutoff = (datetime.utcnow() - timedelta(hours=24)).isoformat()
    existing_data = [entry for entry in existing_data if entry['timestamp'] > cutoff]

    # Save data
    os.makedirs('data', exist_ok=True)
    with open(data_file, 'w') as f:
        json.dump(existing_data, f, indent=2)

if __name__ == '__main__':
    fetch_tsm_data()
