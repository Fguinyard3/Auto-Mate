from rest_framework import serializers
from .models import FacebookUser

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacebookUser
        fields = ['email', 'username', 'first_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop['password']
        user = self.Meta.model(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacebookUser
        fields = ['email','username','first_name']


