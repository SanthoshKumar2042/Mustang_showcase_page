from django.db import models


class contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    pwd = models.CharField(max_length=20)

    def __str__(self):
        return self.name
