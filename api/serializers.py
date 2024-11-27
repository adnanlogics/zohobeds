from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class BookingSerializer(serializers.Serializer):
    roomId = serializers.IntegerField(required=True)
    bookId = serializers.CharField(required=False)
    arrivalFrom = serializers.DateField(required=False)
    arrivalTo = serializers.DateField(required=False)