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
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer


class DiagnosesViewSet(ModelViewSet):
    queryset = Diagnoses.objects.all()
    serializer_class = DiagnosesSerializer


class PacientViewSet(ModelViewSet):
    queryset = Pacient.objects.all()[:3]
    permission_classes = (
        IsAuthenticated,
        IsDoctorOrReadOnly,
    )

    def get_serializer_class(self):
        if self.action == "create":
            return PacientSerializer
        return PacientReadSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
