from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, views, viewsets
from repositories.models import Repository, Set, Record, Property, RecordProperty, RecordSet
from repositories.serializers import RecordSerializer, RepositorySerializer, PropertySerializer

import json

# Create your views here.
class RecordViewSet(viewsets.ModelViewSet):
	queryset = Record.objects.all()
	serializer_class = RecordSerializer

	def create(self, request, repositories_pk=None, format=None):
		# Get data
		data = json.loads(request.body)

		try :

			# Get repository
			repository = Repository.objects.get(pk=repositories_pk)

			# Create record
			r = Record(repository=repository)
			r.save()

			# Set properties
			for property in data:
				if property.has_key('value'):
					p = Property.objects.get(pk=property['id'])
					rp = RecordProperty(property=p, record=r, value=property['value'])
					rp.save()

			rs = RecordSerializer(r)

			return Response(rs.data, status=status.HTTP_201_CREATED)

		except Exception as error:

			return Response({
				'status': 'Error',
				'message': 'An unexpected error has ocurred',
				'data' : error
			}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
			

class RepositoryViewSet(viewsets.ModelViewSet):
	queryset = Repository.objects.all()
	serializer_class = RepositorySerializer

class PropertyViewSet(viewsets.ModelViewSet):
	queryset = Property.objects.all()
	serializer_class = PropertySerializer