from django.db import models
import time

class PaymentModel(models.Model):
    SILVER = "S"
    PLATINUM = "P"
    RUBY = "R"
    STAR = "S"
    GOLD_STAR = "G"
    OPAL = "O"
    DIAMOND = "D"
    PREMIUM = "M"

    PACKAGES = (
        (SILVER, "Silver"),
        (PLATINUM, "Platinum"),
        (RUBY, "Ruby"),
        (STAR, "Star"),
        (GOLD_STAR, "Gold Star"),
        (OPAL, "Opal"),
        (DIAMOND, "Diamond"),
        (PREMIUM, "Premium"),
    )

    PACKAGES_PRICES = {
        SILVER: (5000, 258.33),
        PLATINUM: (10000, 516.66),
        RUBY: (20000, 1033.33),
        STAR: (40000, 2066.66),
        GOLD_STAR: (80000, 4133.33),
        OPAL: (160000, 6266.66),
        DIAMOND: (320000, 16533.33),
        PREMIUM: (640000, 33000.60)
    }

    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("UserModel", on_delete=models.CASCADE, related_name="payments")
    package = models.CharField(max_length=1, choices=PACKAGES)
    
    def __str__(self):
        return self.user.fullname
        
    @property
    def dict(self):
        return {
            "id": self.id,
            "packagePrice": self.PACKAGES_PRICES[self.package][0],
            "createdOn": self.created_on.timestamp() * 1000,
            "package": self.get_package_display(),
            "isActive": time.time() - self.created_on.timestamp() < 3600 * 24 * 30
        }

    class Meta:
        verbose_name = "Payment"
        ordering = ["-created_on"]