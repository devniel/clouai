from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from authentication.models import User
from repositories.models import Property, RecordProperty, Record, Repository

class PropertySerializer(serializers.ModelSerializer):
	class Meta:
		model = Property

class RecordPropertySerializer(serializers.ModelSerializer):
	id = serializers.ReadOnlyField(source='property.id')
	name = serializers.ReadOnlyField(source='property.name')

	class Meta:
		model = RecordProperty
		fields = ('id', 'name', 'value')


class RecordSerializer(serializers.ModelSerializer):
	id = serializers.ReadOnlyField()
	repository = serializers.ReadOnlyField(source='repository.id')
	properties = RecordPropertySerializer(source='recordproperty_set', many=True)
	
	class Meta:
		model = Record
		fields = ('id', 'repository', 'properties')


class RepositorySerializer(serializers.ModelSerializer):
	records = RecordSerializer(source='record_set', many=True)

	class Meta:
		model = Repository
		fields = ('id','name','owner', 'records')