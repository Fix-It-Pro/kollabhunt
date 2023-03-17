import json
import os
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from .adapters import KollabGoogleOAuth2Adapter, KollabGithubOAuth2Adapter
import requests


UserModel = get_user_model()


class GoogleLogin(SocialLoginView):
    adapter_class = KollabGoogleOAuth2Adapter
    callback_url = 'http://127.0.0.1:8000/auth/callback/google/'
    client_class = OAuth2Client


class GithubLogin(SocialLoginView):
    adapter_class = KollabGithubOAuth2Adapter
    callback_url = os.environ.get('GITHUB_CALLBACK'),
    client_class = OAuth2Client


class AuthCallback(object):
    def __init__(self, request, provider):
        self.request = request
        self.provider = provider

    def get_auth_url(self):
        return self.request.scheme+"://"+self.request.get_host()+'/auth/'+self.provider+'/'

    def google_payload(self):
        data = dict()
        if self.request.GET.get('code'):
            data['code'] = self.request.GET.get('code')
        if self.request.GET.get('access_token'):
            data['access_token'] = self.request.GET.get('access_token')
        return data

    def execute(self):
        data_func = getattr(self, self.provider+'_payload')
        response = requests.post(self.get_auth_url(), data_func())
        return response


def callback(request, provider):
    response = AuthCallback(request, provider).execute()
    return response



@csrf_exempt
def github_callback(request):
    a=1
    bc=3
