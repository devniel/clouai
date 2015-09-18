from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from authentication.models import User
from repositories.models import Repository
from repositories.serializers import RepositorySerializer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)
    repositories = RepositorySerializer(source='repository_set', many=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'created_at', 'updated_at', 'password',
                  'confirm_password', 'repositories')
        read_only_fields = ('created_at', 'updated_at', 'repositories')

        def create(self, validated_data):
            return User.objects.create(**validated_data)

        def update(self, instance, validated_data):
            password = validated_data.get('password', None)
            confirm_password = validated_data.get('confirm_password', None)

            if password and confirm_password and password == confirm_password:
                instance.set_password(password)
                instance.save()

            update_session_auth_hash(self.context.get('request'), instance)

            return instance