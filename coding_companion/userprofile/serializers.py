from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)
    profile = ProfileSerializer()
    date_joined = serializers.DateTimeField(read_only=True)
    email = serializers.EmailField()

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        profile_data = validated_data.pop('profile', {})
        profile_data['user'] = user
        profile = Profile.objects.create(**profile_data)
        profile.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
        instance.save()
        profile_data = validated_data.get('profile', {})
        profile = instance.profile
        profile.phone_number = profile_data.get(
            'phone_number', profile.phone_number)
        profile.is_paid = profile_data.get('is_paid', profile.is_paid)
        profile.save()
        return instance

    class Meta:
        model = User
        fields = ["id", "email", "username",
                  "password", "date_joined", "profile"]
