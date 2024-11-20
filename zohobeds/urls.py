from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import home  # Import the view

# Define schema_view before urlpatterns
schema_view = get_schema_view(
    openapi.Info(
        title="Zohobeds API",
        default_version='v1',
        description="API documentation for the Zohobeds project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@zohobeds.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Use 'api.urls', not 'apps.api.urls'
    path('users/', include('users.urls')),  # Include user-related routes
    path('', home, name='home'),
    # Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # ReDoc
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
