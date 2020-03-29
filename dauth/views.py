from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .models import DUser
from .serializer import UserSerializer,ChangePasswordSerializer

# Create your views here.

class UserListCreate(generics.ListCreateAPIView):
    queryset = DUser.objects.all()
    permission_classes = []
    serializer_class = UserSerializer

class UserRetriveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = DUser.objects.all()
    permission_classes = []
    serializer_class = UserSerializer

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = DUser
    permission_classes = []

    def get_object(self, queryset=None):
        obj =  self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("currentPassword")):
                return Response({"currentPassword": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'user': {
                    'id': self.object.id,
                    'username': self.object.username,
                    'role': self.object.groups.values_list('name', flat=True)[0],
                    'roleName': self.object.groups.values_list('name', flat=True)[0].split('_')[1]
                },
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
