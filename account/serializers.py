from rest_framework import serializers
from .helpers import send_spam

from .models import User

class RegisterUserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(min_length=1, required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email','phone', 'password', 'password_confirm' )

    def validate(self, attrs):
        pass1 = attrs.get('password')
        pass2 = attrs.pop('password_confirm')
        if pass1 != pass2:
            raise serializers.ValidationError("Passwords don't match!")
        return attrs
    
    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("User with this email already exists")
        return email
    
    def create(self, validated_data):
        send_spam(User)
        return User.objects.create_user(**validated_data)
    