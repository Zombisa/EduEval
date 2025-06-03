# auth/serializers.py

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        #  Agrega roles al payload del token
        token['roles'] = list(user.groups.values_list('name', flat=True))

        # Puedes agregar más datos si lo necesitas
        token['username'] = user.username
        return token
