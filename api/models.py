from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=255)
    property_id = models.CharField(max_length=50, unique=True)
    api_source = models.CharField(max_length=50)  # e.g., Beds24 or Zoho
    created_at = models.DateTimeField(auto_now_add=True)
