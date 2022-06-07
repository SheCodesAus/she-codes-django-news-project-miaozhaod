from django.urls import path
from .views import CreateAccountView, ViewAccountView

app_name = "users"

urlpatterns = [
    path("create-account/", CreateAccountView.as_view(), name="createAccount"),
    path("view-account/<int:pk>/", ViewAccountView.as_view(), name="viewAccount"),
]
