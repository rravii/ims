from rest_framework import serializers
from .models import DUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group

class ChangePasswordSerializer(serializers.Serializer):
    model = DUser
    currentPassword = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = DUser.objects.create(
            username=validated_data.get('username'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            password=make_password(validated_data.get('password')),
            email=validated_data.get('email'),
            hospital=validated_data.get('hospital'),
            is_active = validated_data.get('is_active')
        )
        if (Group.objects.filter(id=validated_data.get('role'))):
            group = Group.objects.get(pk=validated_data.get('role'))
            group.user_set.add(user)
        else:
            group = Group.objects.filter(name='ROLE_STAFF')[0] if Group.objects.filter(
                name='ROLE_STAFF') else Group.objects.create(name='ROLE_STAFF')
            group.user_set.add(user)
            # validated_data['password'] = make_password(validated_data['password'])
        return user

    class Meta:
        #fields = '__all__'
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'password',
            'email',
            'hospital',
            'is_active',
            'joined'
        ]
        model = DUser