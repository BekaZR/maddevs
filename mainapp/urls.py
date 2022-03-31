from django.urls import path

from rest_framework.routers import SimpleRouter

from mainapp.views import (
    UserRefistrationCreateAPIView,
    DiagnosesViewSet,
    PacientViewSet,
    CustomTokenObtainPairView,
)
from rest_framework_simplejwt.views import TokenRefreshView

# Create router
router = SimpleRouter()

# Register usrl in router
router.register("diagnoses", DiagnosesViewSet, basename="diagnos")
router.register("pacients", PacientViewSet, basename="pacient")


urlpatterns = [
    path("registration/", UserRefistrationCreateAPIView.as_view(), name="registration"),
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

# Add all urls from router to urlpatterns
urlpatterns += router.urls
