from django.db import models

class TodoTask(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self) -> str:
        return self.title