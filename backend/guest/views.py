from django.shortcuts import render
from rest_framework import generics, mixins
from .serializers import GuestSerializer
from .models import Guest
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

class ListCreateGuestView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    serializer_class = GuestSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Guest.objects.all()
    
    @swagger_auto_schema(
        operation_summary="Add a guest",
        operation_description="This adds a new guest"
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="List all guests",
        operation_description="This returns a list of all guests"
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    
class RetrieveUpdateEditDeleteGuestView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = GuestSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Guest.objects.all()
    
    @swagger_auto_schema(
        operation_summary="Retrieve a single guest",
        operation_description="This retrieves a single guest by their ID"
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Update guest's information",
        operation_description="This updates a single guests information by their ID"
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Partially update guest's information",
        operation_description="This updates single elements of a single guest, eg: first_name, etc"
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Delete a single guest",
        operation_description="This deletes a single guest by thier ID"
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)