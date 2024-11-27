from django.urls import path
from .views import PropertyView
from rest_framework.routers import DefaultRouter
from .beds24.views import GetBookingsView, CreateBookingView, GetPropertiesView,CreatePropertiesView


router = DefaultRouter()

urlpatterns = [
    #path('properties/', PropertyView.as_view(), name='properties'),
    path('bookings/', GetBookingsView.as_view(), name='get_bookings'),
    path('bookings/create/', CreateBookingView.as_view(), name='create_booking'),
    path('properties/', GetPropertiesView.as_view(), name='get_properties'),
    path('properties/create/', CreatePropertiesView.as_view(), name='create_properties'),

]

urlpatterns += router.urls