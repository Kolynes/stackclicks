from django.db import models

class TaskModel(models.Model):
    url = models.TextField()
    title = models.CharField(max_length=200)
    body = models.TextField()
    completed_by = models.ManyToManyField("UserModel", related_name="completed_tasks", editable=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        
    @property
    def dict(self):
        return {
            "url": self.url,
            "title": self.title,
            "body": self.body,
            "createdOn": self.created_on.timestamp() * 1000,
            "id": self.id
        }

    class Meta:
        verbose_name = "Task"
        ordering = ["-created_on"]