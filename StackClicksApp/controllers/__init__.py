from django.urls import path
from .AccountsController import AccountsController

urlpatterns = [
    path("accounts/", AccountsController())
]