from rest_framework import permissions, authentication
import jwt
from core.settings import SECRET_KEY


class IsDoctorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        auth_data = authentication.get_authorization_header(request)
        if not auth_data:
            return False
        prefix, token = auth_data.decode("utf-8").split(" ")
        payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")["is_doctor"]

        return payload
