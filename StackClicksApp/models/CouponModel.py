from django.db import models
from utils.code_generator import generate_number_code
from . import PaymentModel

class CouponModel(models.Model):

    number = models.CharField(max_length=16, null=True, blank=True, unique=True)
    vendor = models.ForeignKey("VendorModel", on_delete=models.CASCADE)
    package = models.CharField(max_length=1, choices=PaymentModel.PACKAGES)
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
        return "%s - %s N%s" %(self.vendor.name, self.get_package_display(), PaymentModel.PACKAGES_PRICES[self.package][0])

    def save(self, *args, **kwargs):
        if self.number == None:
            while True:
                self.number = generate_number_code(16)
                if CouponModel.objects.filter(number=self.number).count() == 0:
                    break
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Coupon"