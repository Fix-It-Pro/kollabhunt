from django.urls import path, include, re_path
from .views import GoogleLogin, GithubLogin, github_callback, callback


urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('google/', GoogleLogin.as_view(), name='google_login'),
    path('github/', GithubLogin.as_view(), name='github_login'),
    path('github/callback/', github_callback, name='github_callback'),
    path('callback/<str:provider>/', callback, name='auth_callback')
]