from rest_framework import generics, permissions
from rest_framework.response import Response

from .serializers import userProfileSerializer

# user API
class userProfileAPI(generics.GenericAPIView):
  serializer_class = userProfileSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response({
      "username": userProfileSerializer(user, context=self.get_serializer_context()).data,
      "image": userProfileSerializer(user, context=self.get_serializer_context()).data,
     
    })


