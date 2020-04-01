from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """
    Test ApiView
    """
    serializer_class = serializers.HelloSerializers

    def get(self, request, format=None):
        """
        Returns a list of ApiView features
        :param request:
        :param format:
        :return:
        """
        an_apiview = [
            'Uses HTTP methds as ..',
            'jkljkl jkljkljlk',
            'jkhjkjkjkhjk jhkj',
            'kjkljklkljkljkl',
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview })

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message': message})
        else:
            return Response(serializer.errors,
                            status= status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """
        Handle update
        :param request:
        :param pk:
        :return:
        """
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """

        :param request:
        :param pk:
        :return:
        """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """
        Delete an object
        :param request:
        :param pk:
        :return:
        """
        return Response({'method': 'DELETE'})