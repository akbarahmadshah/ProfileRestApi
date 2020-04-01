from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """
    Test ApiView
    """
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