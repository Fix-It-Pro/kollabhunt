import json
from django.contrib.auth import REDIRECT_FIELD_NAME, get_user_model
from social_core.utils import user_is_authenticated
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from social_core.utils import user_is_authenticated
from social_django.utils import psa
from social_django.views import _do_login, NAMESPACE
from django.contrib.auth import logout as log_out

UserModel = get_user_model()


def do_complete(backend, login, user=None, redirect_name='next',
                *args, **kwargs):
    data = backend.strategy.request_data()

    is_authenticated = user_is_authenticated(user)
    user = user if is_authenticated else None
    auth_details = backend.complete(user=user, *args, **kwargs).auth_details
    request = backend.strategy.request
    email = auth_details.get("email", None)

    payload = {
        "auth_uid": auth_details.get("user_id", None),
        "email": email.lower() if email else ''
    }


@never_cache
@csrf_exempt
@psa()
def complete(request, backend, *args, **kwargs):
    """Authentication complete view"""

    return do_complete(request.backend, _do_login, user=request.user,
                       redirect_name=REDIRECT_FIELD_NAME, request=request,
                       *args, **kwargs)
