from django.utils.deprecation import MiddlewareMixin
from settings.base import URIS_TO_IGNORE_FOR_TOKEN_AUTH
from custom_auth_backend.jwt.token import Token, SIMPLE_JWT
from django.contrib.auth import get_user
from src.utils import HttpStatus, HttpResponse

class AuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path not in URIS_TO_IGNORE_FOR_TOKEN_AUTH:
            assert hasattr(request, 'token'), (
                "The Custom authentication middleware requires token middleware "
                "to be installed. Edit your MIDDLEWARE setting to insert "
                "'custom_middlewares.token.TokenMiddleware' before "
                "'custom_middlewares.authentication.AuthenticationMiddleware'."
            )
            claims = Token.get_claims(request.token)
            if isinstance(claims,HttpResponse):
                return claims
            request.auth_id = claims['auth_id']