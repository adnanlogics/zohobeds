from django.urls import path
from .views import PropertyView
from rest_framework.routers import DefaultRouter
from .beds24.views import GetBookingsView, CreateBookingView, GetPropertiesView,CreatePropertiesView
from .zoho.views import ZohoGetContactsView,ZohoAddDealView

router = DefaultRouter()

urlpatterns = [
    #path('properties/', PropertyView.as_view(), name='properties'),
    path('bookings/', GetBookingsView.as_view(), name='get_bookings'),
    path('bookings/create/', CreateBookingView.as_view(), name='create_booking'),
    path('properties/', GetPropertiesView.as_view(), name='get_properties'),
    path('properties/create/', CreatePropertiesView.as_view(), name='create_properties'),

     # Zoho API endpoints
    path('zoho/contacts/', ZohoGetContactsView.as_view(), name='zoho_get_contacts'),
    path('zoho/deal/create/', ZohoAddDealView.as_view(), name='zoho_add_deal'),

]

urlpatterns += router.urls