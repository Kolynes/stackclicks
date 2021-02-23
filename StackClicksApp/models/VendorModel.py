from django.db import models

class VendorModel(models.Model):
    name = models.CharField(max_length=100)
    whatsapp_link = models.TextField()

    def __str__(self):
        return self.name
        
    @property
    def dict(self):
        return {
            "name": self.name,
            "whatsappLink": self.whatsapp_link
        }

    class Meta:
        verbose_name = "Vendor"