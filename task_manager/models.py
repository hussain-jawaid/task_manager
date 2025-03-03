from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title