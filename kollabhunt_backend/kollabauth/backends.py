from social_core.backends.google import GoogleOAuth2 as BaseGoogleAuth
from django.contrib.auth import get_user_model
from social_core.utils import url_add_parameters


class GoogleOAuth2(BaseGoogleAuth):
    ACCESS_TOKEN_URL = 'https://oauth2.googleapis.com/token'
    def get_redirect_uri(self, state=None):
        """Build redirect with redirect_state parameter."""
        http = self.redirect_uri.split('//')
        uri_parts = http[1].split('/')
        uri_parts[2] = 'auth-complete'
        uri_parts = '/'.join(uri_parts)
        uri = http[0]+'//'+uri_parts

        if self.REDIRECT_STATE and state:
            uri = url_add_parameters(uri, {'redirect_state': state})
        return uri
    def get_user_details(self, response):
        """Return user details from Google account"""
        fullname, first_name, last_name = self.get_user_names(
            response.get('name', ''),
        )
        username = fullname
        return {
            'username': response.get('fullname', ''),
            'email': response.get('email', ''),
            'fullname': fullname,
            'firstname': first_name,
            'lastname': last_name,
        }
