from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object"""
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'wedding_date', 'partner_name', 'wedding_location')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        """Create a new user with an encrypted password and return it"""
        return User.objects.create_user(**validated_data) 