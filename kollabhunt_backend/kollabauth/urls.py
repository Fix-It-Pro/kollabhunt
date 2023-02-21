from django.urls import path, include, re_path
from .views import complete
from social_django.urls import extra

urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
    re_path(r'^auth-complete/(?P<backend>[^/]+){0}$'.format(extra), complete,
            name='auth-complete')
]