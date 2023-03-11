import json
import os
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client


UserModel = get_user_model()


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    # callback_url = CALLBACK_URL_YOU_SET_ON_GOOGLE
    client_class = OAuth2Client


class GithubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = os.environ.get('GITHUB_CALLBACK'),
    client_class = OAuth2Client


@csrf_exempt
def github_callback(request):
    a=1
    bc=3
