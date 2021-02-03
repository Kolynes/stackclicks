from utils.controller import Controller
from utils.decorators import ensure_signed_in
from utils.shortcuts import json_response

class AccountsController(Controller):

    @Controller.route()
    @Controller.decorate(ensure_signed_in)
    def ping(self, request):
        return json_response(True, data=request.user.dict)
