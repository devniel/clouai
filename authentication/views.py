import json

from django.contrib.auth import authenticate, login, logout

from rest_framework import permissions, viewsets

from authentication.models import User
from authentication.permissions import IsAccountOwner
from authentication.serializers import UserSerializer
from pprint import pprint

from rest_framework.response import Response
from rest_framework import status, views

import re

from validate_email import validate_email

class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):        
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            try:
                # Check username
                if not re.match("^[a-z]*$", serializer.validated_data.get('username').lower()):
                    return Response({
                        'status': 'Bad request',
                        'message': 'Account could not be created with received data.',
                        'data' : {'error' : 'Repository name should be composed of letters only.'}
                    }, status=status.HTTP_400_BAD_REQUEST)

                # Check email
                if validate_email(serializer.validated_data.get('email')):
                    return Response({
                        'status': 'Bad request',
                        'message': 'Account could not be created with received data.',
                        'data' : {'error' : 'Invalid email.'}
                    }, status=status.HTTP_400_BAD_REQUEST)

                serializer.validated_data['username'] = serializer.validated_data.get('username').lower()
                User.objects.create_user(**serializer.validated_data)
                return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
            except Exception as error:
                return Response({"Error" : error}, status=500)

        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.',
            'data' : serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)



class LoginView(views.APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)

        email = data.get('email', None)
        password = data.get('password', None)

        user = authenticate(email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                serialized = UserSerializer(user)

                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This user has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)



class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        logout(request)

        return Response({}, status=status.HTTP_204_NO_CONTENT)