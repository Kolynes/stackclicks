from django.urls import path
from .AccountsController import AccountsController
from .TasksController import TasksController
from .PaymentsController import PaymentsController
from .WithdrawalRequestsController import WithdrawalRequestsController
from .VendorsController import VendorsController
from .MessagesController import MessagesController

urlpatterns = [
    path("accounts/", AccountsController()),
    path("payments/", PaymentsController()),
    path("withdrawal_requests/", WithdrawalRequestsController()),
    path("vendors/", VendorsController()),
    path("tasks/", TasksController()),
    path("messages/", MessagesController()),
]