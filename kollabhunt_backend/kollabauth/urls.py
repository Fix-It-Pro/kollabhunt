from django.urls import path, include


urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
]