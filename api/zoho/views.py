import requests
from django.conf import settings
from django.http import JsonResponse
from .utils import save_tokens
from rest_framework.views import APIView
from rest_framework.response import Response
from .services import ZohoAPIService
from rest_framework.parsers import JSONParser

def zoho_callback(request):
    code = request.GET.get("code")
    if not code:
        return JsonResponse({"error": "Authorization code not found"}, status=400)
    
    data = {
        "grant_type": "authorization_code",
        "client_id": settings.ZOHO_CLIENT_ID,
        "client_secret": settings.ZOHO_CLIENT_SECRET,
        "redirect_uri": settings.ZOHO_REDIRECT_URI,
        "code": code,
    }
    response = requests.post(settings.ZOHO_TOKEN_URL, data=data)
    tokens = response.json()
    
    if "access_token" in tokens:
        save_tokens(tokens)
        return JsonResponse({"message": "Tokens saved successfully"})
    return JsonResponse({"error": tokens.get("error", "Unknown error")}, status=400)

class ZohoGetContactsView(APIView):
    def get(self, request):
        try:
            zoho_service = ZohoAPIService()
            contacts = zoho_service.get_contacts()
            return Response(contacts, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=400)
        
class ZohoAddDealView(APIView):
    parser_classes = [JSONParser]

    def post(self, request):
        try:
            deal_data = request.data
            zoho_service = ZohoAPIService()
            deal_response = zoho_service.create_deal(deal_data)
            return Response(deal_response, status=201)
        except Exception as e:
            return Response({"error": str(e)}, status=400)