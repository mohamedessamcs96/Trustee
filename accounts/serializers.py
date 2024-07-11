from rest_framework import serializers
from .models import CustomUser
from django_countries.serializer_fields import CountryField
from .models import CustomUser, Interest

class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ('id', 'name')

class CustomUserSerializer(serializers.ModelSerializer):
    interests = InterestSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'email', 'birthdate', 'country', 'interests')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        interests_data = validated_data.pop('interests', [])
        user = CustomUser.objects.create_user(**validated_data)
        
        # Adding interests to the user
        for interest_data in interests_data:
            interest_obj, created = Interest.objects.get_or_create(name=interest_data['name'])
            user.interests.add(interest_obj)

        return user