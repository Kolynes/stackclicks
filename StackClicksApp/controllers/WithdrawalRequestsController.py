from utils.controller import Controller
from utils.decorators import ensure_signed_in, ensure_post

from utils.shortcuts import json_response, paginate
from StackClicksApp import models

class WithdrawalRequestsController(Controller):

    @Controller.route()
    @Controller.decorate(ensure_signed_in, )
    def get(self, request):
        page = request.GET.get("page", 1)
        data, previousPage, nextPage, numberOfPages = paginate([
            withdrawalRequest.dict for withdrawalRequest in models.WithdrawalRequestModel.objects.filter(user=request.user)
        ], page)
        return json_response(
            200, 
            data=data, 
            number_of_pages=numberOfPages,
            previous_page=previousPage,
            next_page=nextPage
        )
    
    @Controller.route()
    @Controller.decorate(ensure_signed_in, ensure_post)
    def request_withdrawal(self, request):
        if request.POST["type"] == models.WithdrawalRequestModel.BALANCE:
            if float(request.user.balance) < float(request.POST["amount"]):
                return json_response(409, error={
                    "summary": "Insufficient funds"
                })
            elif float(request.user.balance) < 500:
                return json_response(409, error={
                    "summary": "Balance should be more thatn N500 to withdraw"
                })
        if request.POST["type"] == models.WithdrawalRequestModel.REFERRAL:
            if request.user.referral_balance < float(request.POST["amount"]):
                return json_response(409, error={
                    "summary": "Insufficient funds"
                })
            elif request.user.referral_balance < 10000:
                return json_response(409, error={
                    "summary": "Referral balance should be more thatn N10,000 to withdraw"
                })
        all_user_request = request.user.withdrawals.all()
        if len(all_user_request) > 0:
            last_request = all_user_request[0]
            if last_request.status == models.WithdrawalRequestModel.PENDING and last_request.type == request.POST["type"]:
                return json_response(409, error={
                    "summary": "You already have a pending withdrawal request"
                })
        models.WithdrawalRequestModel.objects.create(
            user=request.user,
            status=models.WithdrawalRequestModel.PENDING,
            type=request.POST["type"],
            amount=request.POST["amount"]
        )
        return json_response(201)