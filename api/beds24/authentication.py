from django.conf import settings

def get_auth_headers():
    """
    Returns authentication headers required for Beds24 API.
    """
    return {
        "accept": "application/json",
        "token": settings.BEDS24_API_TOKEN,
    }
