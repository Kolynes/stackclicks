from utils.shortcuts import json_response, paginate
from utils.decorators import ensure_signed_in, ensure_post
from utils.controller import Controller

from utils.paystack import Paystack
from StackClicksApp import models
import os
from dotenv import load_dotenv

dotenv_file = os.path.join(os.path.dirname(__file__), "../../.env")
load_dotenv(dotenv_file)

class PaymentsController(Controller):

    @Controller.route()
    @Controller.decorate(ensure_signed_in, )
    def get(self, request):
        page = request.GET.get("page", 1)
        data, previousPage, nextPage, numberOfPages = paginate([
            payment.dict for payment in request.user.payments.all()
        ], page)
        return json_response(
            200, 
            data=data, 
            number_of_pages=numberOfPages,
            previous_page=previousPage,
            next_page=nextPage
        )
    
    @Controller.route()
    @Controller.decorate(ensure_signed_in, )
    def get_active(self, request):
        if request.user.payments.count() > 0:
            current_payment = request.user.payments.all()[0]
            if current_payment.dict["isActive"]:
                return json_response(
                    200, 
                    data=current_payment.dict, 
                )
            else:
                 return json_response(
                    404,
                    error={
                        "summary": "No active package found"
                    }
                )
        else:
            return json_response(
                404,
                error={
                    "summary": "No active package found"
                }
            )

    @Controller.route()
    @Controller.decorate(ensure_signed_in, ensure_post, )
    def pay(self, request):
        coupon_number = request.POST["coupon"]
        try:
            coupon = models.CouponModel.objects.get(number=coupon_number)
            if coupon.used:
                return json_response(401, error={
                    "summary": "Coupon already used"
                })
            current_payments = models.PaymentModel.objects.filter()
            models.PaymentModel.objects.create(
                user=request.user,
                package=coupon.package
            )
            coupon.used = True
            coupon.save()
            return json_response(201)
        except models.CouponModel.DoesNotExist:
            return json_response(404, error={
                "summary": "Invalid coupon number"
            })