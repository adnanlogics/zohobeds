import requests
from django.conf import settings
from .authentication import get_auth_headers

def get_properties():
    """
    Fetch properties from Beds24 API.
    """
    url = f"{settings.BEDS24_BASE_URL}properties"
    headers = get_auth_headers()
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch properties: {response.json()}")

def create_property(properties_data):
    """
    Create new properties in Beds24 API.
    :param properties_data: List of dictionaries containing property details to create.
    """
    url = f"{settings.BEDS24_BASE_URL}json"
    payload = {
        "authentication": {
            "apiKey": settings.BEDS24_API_KEY,
        },
        "createProperties": properties_data
    }
    headers = {
        "Content-Type": "application/json",
        **get_auth_headers(),
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to create properties: {response.json()}")
