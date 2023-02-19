from django.urls import path, include
from .callback import github_callback

urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
]