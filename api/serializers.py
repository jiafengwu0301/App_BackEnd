
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Account
from rest_framework.exceptions import ValidationError


class AccountCreateSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.username')
    password = serializers.CharField(source='user.password', style={'input_type': 'password'})

    class Meta:
        model = Account
        fields = [
            'id',
            'username',
            'displayName',
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
            'displayName',
            'facebook',
        ]


class AccountRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = [
            'id',
            'username',
            'displayName',
            'facebook',
        ]


class UpdateAccountSerializer(serializers.ModelSerializer):

    password = serializers.CharField(source='user.password', allow_blank=True, allow_null=True)
    facebook = serializers.CharField(allow_blank=True, allow_null=True)
    displayName = serializers.CharField(allow_blank=True, allow_null=True)

    class Meta:
        model = Account
        fields = [
            'displayName',
            'facebook',
            'password'
        ]

    def update(self, instance, validated_data):

        user_data = validated_data.pop('user', None)
        user = User.objects.get(id=instance.user.id)
        instance.displayName = self.value_or_keep(instance.displayName, validated_data.get('displayName', instance.displayName))
        instance.facebook = self.value_or_keep(instance.facebook, validated_data.get('facebook',instance.facebook))
        if user_data['password'] != "":
            user.set_password(user_data['password'])
        user.save()
        instance.save()
        return instance


    @staticmethod
    def value_or_keep(field, value):
        if value == "":
            return field
        return value


class AuthenticateSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.username')
    password = serializers.CharField(source='user.password', style={'input_type': 'password'})
    account = AccountSerializer(allow_null=True, read_only=True)

    class Meta:
        model = User
        depth = 1
        fields = [
            'username',
            'password',
            'account',
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        validation_data = dict(attrs)['user']
        username = validation_data.get('username', None)
        password = validation_data.get('password', None)

        try:
            user = User.objects.get(username=username)

        except:
            raise ValidationError("Incorrect Username/Password")

        if user.check_password(password):
            attrs['account'] = user.account
            return attrs
        raise ValidationError("Incorrect login/password.")
