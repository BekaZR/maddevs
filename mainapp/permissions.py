from rest_framework import permissions, authentication
import jwt
from core.settings import SECRET_KEY


class IsDoctorOrReadOnly(permissions.BasePermission):
    """ 
    Custom IsDoctor permission for check user
    """
    def has_permission(self, request, view):
        # Get prefix with JWT token from headers
        auth_data = authentication.get_authorization_header(request)
        if not auth_data:
            return False
        # Get JWT token
        prefix, token = auth_data.decode("utf-8").split(" ")
        # Get value from field is_doctor
        payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")["is_doctor"]
        
        return payload
