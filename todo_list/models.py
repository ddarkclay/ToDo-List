from django.db import models

class List(models.Model):
    item = models.CharField(max_length=200, default="")
    completed = models.BooleanField(default=True)

    def __str__(self):
        return self.item + ' | ' + str(self.completed)
    