from utils.controller import Controller
from utils.decorators import ensure_signed_in, ensure_post
from utils.shortcuts import json_response


class AccountsController(Controller):

    @Controller.route()
    @Controller.decorate(ensure_signed_in)
    def ping(self, request):
        return json_response(200, data=request.user.dict)

    @Controller.route()
    @Controller.decorate(ensure_signed_in, ensure_post)
    def change_bank_details(self, request):
        request.user.bank_name = request.POST["bank_name"]
        request.user.account_number = request.POST["account_number"]
        request.user.account_name = request.POST["account_name"]
        request.user.save()
        return json_response(200)
