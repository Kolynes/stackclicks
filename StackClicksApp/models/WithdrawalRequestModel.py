from django.db import models
import time

class WithdrawalRequestModel(models.Model):
    REFERRAL = "R"
    BALANCE = "B"

    PENDING = "P"
    SUCCESSFUL = "S"

    STATUS = (
        (PENDING, "Pending"),
        (SUCCESSFUL, "Successful"),
    )

    TYPES = (
        (BALANCE, "Balance"),
        (REFERRAL, "Referral"),
    )

    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("UserModel", on_delete=models.CASCADE, related_name="withdrawals")
    status = models.CharField(max_length=1, choices=STATUS, default=PENDING)
    type = models.CharField(max_length=1, choices=TYPES)
    processed = models.BooleanField(default=False, editable=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.user.fullname
    
    @property
    def dict(self):
        return {
            "id": self.id,
            "type": self.get_type_display(),
            "createdOn": self.created_on.timestamp() * 1000,
            "amount": float(self.amount),
            "status": self.get_status_display(),
        }

    class Meta:
        verbose_name = "Withdrawal Request"
        ordering = ["-created_on"]