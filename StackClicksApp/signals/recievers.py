from django.dispatch import receiver
from AccountsApp import signals
from .. import models
from django.db.models.signals import post_save

@receiver(signals.signed_up)
def on_signed_up(sender, **kwargs):
    kwargs["user"].referral_balance = 1000
    if kwargs["request"].GET.get("r"):
        try:
            referee = models.UserModel.objects.get(referral_code=kwargs["request"].GET.get("r"))
            kwargs["user"].referee = referee
            referee.referral_balance += 50
            referee.save()
        except models.UserModel.DoesNotExist:
            pass
    kwargs["user"].save()

@receiver(post_save, sender=models.WithdrawalRequestModel)
def on_withdrawal_request_successful(sender, instance, **kwargs):
    if not instance.processed and instance.status == models.WithdrawalRequestModel.SUCCESSFUL:
        if instance.type == models.WithdrawalRequestModel.BALANCE:
            instance.user.balance -= instance.amount
        else:
            instance.user.referral_balance -= instance.amount
        instance.processed = True
        instance.user.save()
        instance.save()

@receiver(post_save, sender=models.PaymentModel)
def on_payment(sender, instance, **kwargs):
    if instance.user.payments.count() == 1 and instance.user.referee != None:
        instance.user.referee.referral_balance += models.PaymentModel.PACKAGES_PRICES[instance.pakage][0] * 0.1
        instance.user.referee.save()