import jwt
from rest_framework import authentication, exceptions
from core.settings import SECRET_KEY
from mainapp.models import User


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)

        if not auth_data:
            return None

        prefix, token = auth_data.decode("utf-8").split(" ")
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")

            user = User.objects.get(id=payload["user_id"])
            is_doctor = payload["is_doctor"]
            print("\n\n\n\n\n", user, token, is_doctor, "\n\n\n\n\n")
            return (user, token)

        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed("Your token is invalid,login")
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed("Your token is expired,login")

        return super().authenticate(request)
