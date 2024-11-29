import requests
from django.conf import settings
from .utils import load_tokens, save_tokens

class ZohoAPIService:
    def __init__(self):
        self.base_url = settings.ZOHO_API_BASE_URL
        tokens = load_tokens()
        self.access_token = tokens.get("access_token")
        self.refresh_token = tokens.get("refresh_token")
    
    def get_headers(self):
        return {"Authorization": f"Bearer {self.access_token}"}
    
    def refresh_access_token(self):
        data = {
            "grant_type": "refresh_token",
            "client_id": settings.ZOHO_CLIENT_ID,
            "client_secret": settings.ZOHO_CLIENT_SECRET,
            "refresh_token": self.refresh_token,
        }
        response = requests.post(settings.ZOHO_TOKEN_URL, data=data)
        tokens = response.json()
        if "access_token" in tokens:
            save_tokens(tokens)
            self.access_token = tokens["access_token"]
        else:
            raise Exception("Failed to refresh access token")
    
    def make_request(self, endpoint, method="GET", data=None):
        url = f"{self.base_url}/{endpoint}"
        headers = self.get_headers()
        response = requests.request(method, url, headers=headers, json=data)
        if response.status_code == 401:  # Token expired
            self.refresh_access_token()
            headers = self.get_headers()
            response = requests.request(method, url, headers=headers, json=data)
        return response.json()
    
    def get_contacts(self):
        return self.make_request("Contacts")

    def create_deal(self, deal_data):
        return self.make_request("Deals", method="POST", data=deal_data)
