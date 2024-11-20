from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Property
from .serializers import PropertySerializer

class PropertyView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve a list of all properties",
        responses={200: PropertySerializer(many=True)},
    )
    def get(self, request):
        properties = Property.objects.all()
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new property",
        request_body=PropertySerializer,
        responses={201: PropertySerializer},
    )
    def post(self, request):
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
