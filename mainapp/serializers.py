from rest_framework import serializers, exceptions
from mainapp.models import User, Diagnoses, Pacient
from datetime import timedelta
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class DiagnosesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnoses
        fields = (
            "id",
            "name_diagnos",
        )


class PacientReadSerializer(serializers.ModelSerializer):
    diagnoses = DiagnosesSerializer(many=True, read_only=True)

    class Meta:
        model = Pacient
        fields = (
            "id",
            "date_of_birth",
            "created_at",
            "diagnoses",
        )
        read_only_fields = ("created_at",)


class PacientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacient
        fields = (
            "id",
            "date_of_birth",
            "diagnoses",
        )
        read_only_fields = ("created_at",)


class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    is_doctor = serializers.BooleanField(default=False)

    def validated_password(self, value):
        if len(value) < 5:
            raise exceptions.ValidationError("Password is too short")
        elif len(value) > 20:
            raise exceptions.ValidationError("Password is too long")
        return value

    def create(self, validated_data):
        if User.objects.filter(username=validated_data.get("username")).exists():
            raise exceptions.ValidationError(
                {"Message": "User with such username is already exists"}
            )

        user = User.objects.create(
            username=validated_data.get("username"),
            is_doctor=validated_data.get("is_doctor"),
        )

        user.set_password(validated_data.get("password"))
        user.save()

        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(CustomTokenObtainPairSerializer, cls).get_token(user)
        token.set_exp(lifetime=timedelta(days=10))
        token["is_doctor"] = user.is_doctor
        return token
