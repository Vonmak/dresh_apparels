from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MerchantSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    location = serializers.CharField(required=True)
    password1 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'}, min_length=6)
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'}, min_length=6)

    def validate(self, data):
        """
        Validates that the two password fields match.
        """
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("The two password fields must match.")
        return data
    

class CustomerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password1 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'}, min_length=6)
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'}, min_length=6)
    
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
    
    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError("The two password fields didn't match.")
        return attrs
    


class LoginSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if not email or not password:
            raise serializers.ValidationError('Must include both email and password.')

        user = authenticate(request=self.context.get('request'), email=get_user_model().objects.get(email=email), password=password)

        if not user:
            raise serializers.ValidationError('Unable to log in with provided credentials.')

        refresh = self.get_token(user)
        return {'refresh': str(refresh), 'access': str(refresh.access_token)}
