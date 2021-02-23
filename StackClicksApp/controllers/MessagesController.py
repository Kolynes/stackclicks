from utils.controller import Controller
from utils.decorators import ensure_signed_in
from utils.shortcuts import json_response
from StackClicksApp import models

class MessagesController(Controller):

    @Controller.route()
    @Controller.decorate(ensure_signed_in)
    def get(self, request):
        messages = models.MessageModel.objects.all()
        if len(messages) > 0:
            return json_response(200, data=messages[0].dict)
        else:
            return json_response(404, error={
                "summary": "No messages found"
            })

