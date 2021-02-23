from django.db import models

class MessageModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    @property
    def dict(self):
        return {
            "createdOn": self.created_on.timestamp() * 1000,
            "message": self.message
        }

    class Meta:
        ordering = ["-created_on"]
        verbose_name = "Message"