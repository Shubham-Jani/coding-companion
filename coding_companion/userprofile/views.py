from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, mixins, generics, response, status
from .serializers import UserSerializer
from django.contrib.auth.models import User


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            return Response({"staff_error": "use admin page to handle this profile"})
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return Response({"staff_error": "use admin page to handle this profile"})
        serializer = UserSerializer(
            request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        if request.user.is_staff:
            return Response({"staff_error": "use admin page to handle this profile"})
        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
