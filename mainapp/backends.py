import jwt
from rest_framework import authentication, exceptions
from core.settings import SECRET_KEY
from mainapp.models import User


class JWTAuthentication(authentication.BaseAuthentication):
    """ 
    Create custom authenticate method for decode JWT token
    """
    def authenticate(self, request):
        # Get user data from headers
        auth_data = authentication.get_authorization_header(request)
        # Check nullable data or not
        if not auth_data:
            return None
        # Get JWT token
        prefix, token = auth_data.decode("utf-8").split(" ")
        try:
            # Decode JWT token
            payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")
            # Get user by id from decode payload
            user = User.objects.get(id=payload["user_id"])
            return (user, token)

        # Check decode exceptions
        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed("Your token is invalid,login")
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed("Your token is expired,login")

        return super().authenticate(request)
