from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from .povider import KollabGoogleProvider, KollabGithubProvider


class KollabSocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin,data)
        return user


class KollabGoogleOAuth2Adapter(GoogleOAuth2Adapter):
    provider_id = KollabGoogleProvider.id
    def get_provider(self):
        return KollabGoogleProvider(self.request)


class KollabGithubOAuth2Adapter(GitHubOAuth2Adapter):
    provider_id = KollabGithubProvider.id
    def get_provider(self):
        return KollabGithubProvider(self.request)
