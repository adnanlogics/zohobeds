from django.shortcuts import redirect
from django.conf import settings

def zoho_auth(request):
    auth_url = (
        f"{settings.ZOHO_AUTH_URL}?response_type=code&client_id={settings.ZOHO_CLIENT_ID}"
        f"&scope=ZohoCRM.modules.ALL&redirect_uri={settings.ZOHO_REDIRECT_URI}"
    )
    return redirect(auth_url)