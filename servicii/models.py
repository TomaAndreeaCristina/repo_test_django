from django.db import models

# Create your models here.
class ServiciiModel(models.Model):
    nume= models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=300, null=False)

    def __str__(self):
        return f"{self.nume} - {self.description}"