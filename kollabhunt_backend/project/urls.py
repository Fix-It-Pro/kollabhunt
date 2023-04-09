from django.urls import path, include
from .views import ProjectAPIView
urlpatterns = [
    path('', ProjectAPIView.as_view(), name='project_apiview'),
]