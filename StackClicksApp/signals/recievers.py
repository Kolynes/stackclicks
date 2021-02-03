from django.dispatch import receiver
from AccountsApp import signals
from .. import models

@receiver(signals.signed_up)
def on_signed_up(sender, **kwargs):
    if kwargs["request"].GET.get("r"):
        try:
            referee = models.UserModel.objects.get(referral_code=kwargs["request"].GET.get("r"))
            kwargs["user"].referee = referee
            kwargs["user"].save()
        except models.UserModel.DoesNotExist as e:
            pass