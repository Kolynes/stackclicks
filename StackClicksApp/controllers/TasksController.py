from utils.shortcuts import json_response, paginate
from utils.controller import Controller
from utils.decorators import ensure_signed_in, ensure_post

from StackClicksApp import models

class TasksController(Controller):

    @Controller.route()
    @Controller.decorate(ensure_signed_in, ensure_post)
    def complete(self, request):
        try:
            task = models.TaskModel.objects.get(id=request.POST["id"])
            if(request.user not in task.completed_by.all()):
                task.completed_by.add(request.user)
                current_payment = request.user.payments.all()[0]
                if not current_payment.dict["isActive"]:
                    return json_response(409, error={
                        "summary": "No active package found"
                    })
                request.user.balance += models.PaymentModel.PACKAGES_PRICES[current_payment.package][1]
                task.save()
                request.user.save()
            return json_response(200)
        except models.TaskModel.DoesNotExist:
            return json_response(404, error={
                "summary": "Task not found"
            })

    @Controller.route()
    @Controller.decorate(ensure_signed_in)
    def get(self, request):
        if models.TaskModel.objects.count() > 0:
            latest_task = models.TaskModel.objects.all()[0]
            return json_response(200, data={
                **latest_task.dict, 
                "completed": request.user in latest_task.completed_by.all()
            })
        else:
            return json_response(404, error={
                "summary": "No tasks found"
            })