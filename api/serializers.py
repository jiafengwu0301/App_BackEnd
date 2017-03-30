
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Account


class AccountCreateSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.username')
    password = serializers.CharField(source='user.password', style={'input_type': 'password'})

    class Meta:
        model = Account
        fields = [
            'id',
            'username',
            'facebook',
            'password',
        ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        user.set_password(user_data['password'])
        user.save()

        account = Account.objects.create(user=user, **validated_data)
        account.username = user.username
        account.save()
        return account


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = [
            'id',
            'username',
            'facebook'
        ]
