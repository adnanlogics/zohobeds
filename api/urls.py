from django.urls import path
from .views import PropertyView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

urlpatterns = [
    path('properties/', PropertyView.as_view(), name='properties'),
]

urlpatterns += router.urls
