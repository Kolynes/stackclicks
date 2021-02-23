from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from StackClicksApp import models

admin.site.register(models.UserModel)