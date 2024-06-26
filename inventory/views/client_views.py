from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import TokenAuthentication
from ..models import Client
from ..serializers import ClientSerializer

class ClientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(
        operation_summary="List all clients",
        responses={200: ClientSerializer(many=True)},
        security=[{"Bearer": []}],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new client",
        request_body=ClientSerializer,
        responses={201: ClientSerializer},
        security=[{"Bearer": []}],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class ClientDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(
        operation_summary="Retrieve a client",
        responses={200: ClientSerializer},
        security=[{"Bearer": []}],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a client",
        request_body=ClientSerializer,
        responses={200: ClientSerializer},
        security=[{"Bearer": []}],
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a client",
        responses={204: None},
        security=[{"Bearer": []}],
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
