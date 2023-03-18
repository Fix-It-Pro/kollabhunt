from django.urls import path, include
from .views import GoogleLogin, GithubLogin, callback


urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('google/', GoogleLogin.as_view(), name='google_login'),
    path('github/', GithubLogin.as_view(), name='github_login'),
    path('callback/<str:provider>/', callback, name='auth_callback'),

]