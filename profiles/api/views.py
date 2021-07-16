from profiles.models import Client
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from profiles.api.serializers import ClientSerializer
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated


class ClientCreateAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request: Request) -> Response:
        """
        GET method for Client model.

        Args:
            request (Request): retrieval HttpRequest.

        Returns:
            Response: Http response with every client created.
        """

        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        POST method for Client model.

        Args:
            request (Request): retrieval HttpRequest.

        Returns:
            Response: Http response with the client created.
        """

        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {"Message": "Hello, World!"}
        return Response(content)
