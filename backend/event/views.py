from django.shortcuts import render
from rest_framework import generics, mixins
from .serializers import EventSerializer
from .models import Event
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

class ListCreateEventView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Event.objects.all()
    
    @swagger_auto_schema(
        operation_summary="Create an event",
        operation_description="This creates a new event"
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_summary="List all events",
        operation_description="This returns a list of all events"
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    
class RetrieveUpdateEditDeleteEventView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Event.objects.all()
    
    @swagger_auto_schema(
        operation_summary="Retrieve an event",
        operation_description="This queries an event by its ID and returns the single event "
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Update an event",
        operation_description="This updates an event by its ID"
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Partially update an event",
        operation_description="This updates single elements of a single event, eg: title, location, etc"
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Delete an events",
        operation_description="This deletes an event by its ID"
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)