from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListCreateEventView.as_view(), name="create-list-event"),
    path("<int:pk>", views.RetrieveUpdateEditDeleteEventView.as_view(), name="retrieve-update-delete-event")
]