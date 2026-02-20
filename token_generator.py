import requests

TENANT_ID = "YOUR_TENANT_ID"
CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"

url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"

payload = {
    "client_id": CLIENT_ID,
    "scope": "https://graph.microsoft.com/.default",
    "client_secret": CLIENT_SECRET,
    "grant_type": "client_credentials"
}

response = requests.post(url, data=payload)

if response.status_code == 200:
    print("Access Token Generated Successfully")
    print(response.json()["access_token"])
else:
    print("Error:", response.text) 
