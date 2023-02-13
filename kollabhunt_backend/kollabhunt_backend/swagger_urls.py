from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path as url


schema_view = get_schema_view(
   openapi.Info(
      title="Kollabhunt API",
      default_version='v1',
      description="Kollabhunt Restful API list",
      terms_of_service="https://www.kollabhunt.com/policies/terms/",
      contact=openapi.Contact(email="contact@kollabhunt.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    url(r'^kollabhunt/v1/api/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^kollabhunt/v1/docs/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
