from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from mainapp.serializers import (
    RegistrationSerializer,
    DiagnosesSerializer,
    PacientSerializer,
    PacientReadSerializer,
    CustomTokenObtainPairSerializer,
)
from mainapp.models import (
    User,
    Diagnoses,
    Pacient,
)

from mainapp.permissions import IsDoctorOrReadOnly

from rest_framework_simplejwt.views import TokenObtainPairView


class UserRefistrationCreateAPIView(CreateAPIView):
    """
    Create user registration view
    """
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer


class DiagnosesViewSet(ModelViewSet):
    """
    Full crud diagnoses for pacients
    """
    queryset = Diagnoses.objects.all()
    serializer_class = DiagnosesSerializer


class PacientViewSet(ModelViewSet):
    """ 
    Create pacients and get 3 on action list
    """
    queryset = Pacient.objects.all()[:3]
    # create custom permission for user doctor
    permission_classes = (
        IsAuthenticated,
        IsDoctorOrReadOnly,
    )

    # Rewrite method get_serializer_class for different action
    def get_serializer_class(self):
        if self.action == "create":
            return PacientSerializer
        return PacientReadSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    """ 
    Rewrite class TokenObtainPairView for set custom serializer class
    """
    serializer_class = CustomTokenObtainPairSerializer
