import requests
from django.conf import settings
from .authentication import get_auth_headers

def get_bookings(params=None):
    """
    Fetch bookings from Beds24 API.
    :param params: Optional dictionary of query parameters (e.g., roomId, arrivalFrom).
    """
    url = f"{settings.BEDS24_BASE_URL}bookings"
    headers = get_auth_headers()
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch bookings: {response.json()}")

def add_booking(booking_data):
    """
    Add a booking to Beds24 API.
    :param booking_data: Dictionary containing booking details.
    """
    url = f"{settings.BEDS24_BASE_URL}bookings"
    headers = get_auth_headers()
    response = requests.post(url, headers=headers, json=booking_data)
    if response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Failed to add booking: {response.json()}")
