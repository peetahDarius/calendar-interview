from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListCreateGuestView.as_view(), name="create-list-guest"),
    path("<int:pk>", views.RetrieveUpdateEditDeleteGuestView.as_view(), name="retrieve-update-delete-guest")
]
