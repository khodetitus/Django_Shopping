from rest_framework.views import APIView
from rest_framework.response import Response
from customers.models import Profile
from .serializers import ProfileSerializer
from rest_framework import status


# customers app api views
class ProfileApiView(APIView):
    def get(self, request, user_id):
        user = Profile.objects.get(id=user_id)
        serializer = ProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        return Response


class ProfileEditApiView(APIView):
    def get(self, request, user_id):
        user = Profile.objects.get(id=user_id)
        serializer = ProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        return Response
