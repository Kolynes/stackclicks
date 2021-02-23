from django.db import models
from utils.code_generator import generate_number_code

class CouponModel(models.Model):
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

    number = models.CharField(max_length=16, null=True, blank=True, unique=True)
    vendor = models.ForeignKey("VendorModel", on_delete=models.CASCADE)
    package = models.CharField(max_length=1, choices=PACKAGES)
    used = models.BooleanField(default=False)

    @property
    def dict(self):
        return {
            "number": self.number,
            "vendor": self.vendor.dict,
            "package": self.get_package_display(),
            "used": self.used
        }
    
    def __str__(self):
        return "%s - %s N%s" %(self.vendor.name, self.get_package_display(), CouponModel.PACKAGES_PRICES[self.package][0])

    def save(self, *args, **kwargs):
        if self.number == None:
            while True:
                self.number = generate_number_code(16)
                if CouponModel.objects.filter(number=self.number).count() == 0:
                    break
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Coupon"