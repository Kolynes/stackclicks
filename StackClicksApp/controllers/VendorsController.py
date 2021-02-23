from utils.controller import Controller
from utils.shortcuts import json_response, paginate

from utils.decorators import ensure_signed_in
from StackClicksApp import models

class VendorsController(Controller):

    @Controller.route()
    @Controller.decorate(ensure_signed_in, )
    def get(self, request):
        page = request.GET.get("page", 1)
        data, previousPage, nextPage, numberOfPages = paginate([
            vendor.dict for vendor in models.VendorModel.objects.all()
        ], page)
        return json_response(
            200, 
            data=data, 
            number_of_pages=numberOfPages,
            previous_page=previousPage,
            next_page=nextPage
        )
