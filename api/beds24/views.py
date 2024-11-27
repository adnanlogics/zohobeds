from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .bookings import get_bookings, add_booking
from .properties import get_properties, create_property

class GetBookingsView(APIView):
    def get(self, request):
        try:
            params = request.query_params.dict()
            bookings = get_bookings(params)
            return Response(bookings, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class CreateBookingView(APIView):
    def post(self, request):
        try:
            booking_data = request.data
            booking = add_booking(booking_data)
            return Response(booking, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class GetPropertiesView(APIView):
    def get(self, request):
        try:
            properties = get_properties()
            return Response(properties, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class CreatePropertiesView(APIView):
    """
    API view to create new properties in Beds24.
    """

    def post(self, request):
        try:
            properties_data = request.data.get("createProperties", [])
            if not properties_data:
                return Response(
                    {"error": "No property data provided."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            result = create_property(properties_data)
            return Response(result, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
