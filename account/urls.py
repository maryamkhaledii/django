from django.urls import path
from account.views import *

app_name = "account"

urlpatterns = [
    path("user-register/", RegisterView.as_view(), name="user-register"),
    path("user-login/", LoginView.as_view(), name="user-login"),
    path("user-logout/", LogoutView.as_view(), name="user-logout"),
]