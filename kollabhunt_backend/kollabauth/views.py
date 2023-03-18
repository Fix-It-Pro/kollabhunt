from django.contrib.auth import get_user_model
from django.http import JsonResponse
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
    callback_url = 'http://127.0.0.1:8000/auth/callback/github/'
    client_class = OAuth2Client


class GitHubLoginV2(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter

    def get(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=request.GET)
        self.serializer.is_valid(raise_exception=True)
        self.login()
        return self.get_response()

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() == 'get':
            return self.get(request, *args, **kwargs)
        else:
            return super(GitHubLoginV2, self).dispatch(request, *args, **kwargs)

    def process_login(self):
        user = self.serializer.validated_data['user']

        # Generate access token
        access_token = self.get_response_serializer().get_token(user).access_token

        # Generate refresh token
        refresh_token = self.get_response_serializer().get_token(user).refresh_token

        # Set refresh token cookie
        response = self.get_response()
        response.set_cookie(key='refresh_token', value=str(refresh_token), httponly=True)

        # Return access token in response data
        response_data = {
            'access_token': str(access_token),
            'user_id': user.id,
        }
        return response_data


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

    def github_payload(self):
        data = dict()
        if self.request.GET.get('code'):
            data['code'] = self.request.GET.get('code')
        return data

    def execute(self):
        data_func = getattr(self, self.provider+'_payload')
        response = requests.post(self.get_auth_url(), data_func())
        return response


def callback(request, provider):
    response = AuthCallback(request, provider).execute()
    return JsonResponse(response.json())
