from rest_framework import generics, permissions
from rest_framework.response import Response

from .serializers import PostSerializer

# Post API
class PostAPI(generics.GenericAPIView):
  serializer_class = PostSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response({
      "title": PostSerializer(user, context=self.get_serializer_context()).data,
     
    })


